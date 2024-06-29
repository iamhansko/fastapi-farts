from pydantic import BaseModel, Field

class TaskBase(BaseModel):
  title: str | None=Field(None, example="독서")

class TaskCreate(TaskBase):
  pass

class TaskCreateResponse(TaskCreate):
  id: int
  class Config:
    orm_mode=True # 암묵적으로 ORM에서 DB 모델의 객체를 받아들여 응답 스키마로 변환

class Task(TaskBase):
  id: int
  done: bool=Field(False, description="완료 여부")
  class Config:
    orm_mode=True # 암묵적으로 ORM에서 DB 모델의 객체를 받아들여 응답 스키마로 변환