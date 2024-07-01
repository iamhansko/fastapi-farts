import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import starlette.status

from api.db import get_db, Base
from api.main import app

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
  # 비동기식 DB 접속을 위한 엔진과 세션
  async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
  async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

  # 테스트용 온메모리 SQList 테이블 초기화 (함수별로 재설정)
  async with async_engine.begin() as conn:
    await conn.run_sync(Base.metadata.drop_all)
    await conn.run_sync(Base.metadata.create_all)
  
  # Dependency Injection으로 FastAPI가 테스트용 DB 참조하도록 변경
  async def get_test_db():
    async with async_session() as session:
      yield session
  
  app.dependency_overrides[get_db] = get_test_db

  # 테스트용 비동기 HTTP 클라이언트 반환
  async with AsyncClient(app=app, base_url="http://test") as client:
    yield client

@pytest.mark.asyncio
async def test_create_and_read(async_client):
  response = await async_client.post("/tasks", json={"title": "Test Task"})
  assert response.status_code == starlette.status.HTTP_200_OK
  response_obj = response.json()
  assert response_obj["title"] == "Test Task"

  response = await async_client.get("/tasks")
  assert response.status_code == starlette.status.HTTP_200_OK
  response_obj = response.json()
  assert len(response_obj) == 1
  assert response_obj[0]["title"] == "Test Task"
  assert response_obj[0]["done"] is False

@pytest.mark.asyncio
async def test_done_flag(async_client):
  response = await async_client.post("/tasks", json={"title": "Test Task 2"})
  assert response.status_code == starlette.status.HTTP_200_OK
  response_obj = response.json()
  assert response_obj["title"] == "Test Task 2"

  response = await async_client.put("/tasks/1/done")
  assert response.status_code == starlette.status.HTTP_200_OK

  response = await async_client.put("/tasks/1/done")
  assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST

  response = await async_client.delete("/tasks/1/done")
  assert response.status_code == starlette.status.HTTP_200_OK

  response = await async_client.delete("/tasks/1/done")
  assert response.status_code == starlette.status.HTTP_404_NOT_FOUND

@pytest.mark.asyncio
@pytest.mark.parametrize(
  "input_param, expectation",
  [
    ("2024-12-01", starlette.status.HTTP_200_OK),
    ("2024-12-41", starlette.status.HTTP_422_UNPROCESSABLE_ENTITY),
    ("2024/12/01", starlette.status.HTTP_422_UNPROCESSABLE_ENTITY),
    ("2024-1201", starlette.status.HTTP_422_UNPROCESSABLE_ENTITY),
  ],
)
async def test_due_date(input_param, expectation, async_client):
  response = await async_client.post("/tasks", json={"title":"Test Task","due_date":input_param})
  # print(response.content)
  assert response.status_code == expectation
