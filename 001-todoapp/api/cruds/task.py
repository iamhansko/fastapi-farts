from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

async def create_task(db:AsyncSession, task_create:task_schema.TaskCreate) -> task_model.Task:
  task = task_model.Task(**task_create.dict()) # Python 객체를 DB 모델로 변환
  db.add(task) 
  await db.commit() # DB Commit
  await db.refresh(task) # DB 데이터를 바탕으로 Task 인스턴스인 task 업데이트 (DB에 작성된 레코드 ID 가져옴)
  return task

async def get_task_with_done(db:AsyncSession) -> list[tuple[int, str, bool]]:
  result:Result = await db.execute(
    select(
      task_model.Task.id,
      task_model.Task.title,
      task_model.Done.id.isnot(None).label("done"), # Done.id(o)->done=True, Done.id(x)->done=False
    ).outerjoin(task_model.Done)
  )
  return result.all()

async def get_task(db:AsyncSession, task_id:int) -> task_model.Task | None:
  result: Result = await db.execute(
    select(task_model.Task).filter(task_model.Task.id == task_id)
  )
  return result.scalars().first() # Tuple(Vector) -> Scalar

async def update_task(db:AsyncSession, task_create:task_schema.TaskCreate, original:task_model.Task) -> task_model.Task:
  original.title = task_create.title
  db.add(original)
  await db.commit()
  await db.refresh(original)
  return original

async def delete_task(db:AsyncSession, original:task_model.Task) -> None:
  await db.delete(original)
  await db.commit()