from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db:Session, task_create:task_schema.TaskCreate) -> task_model.Task:
  task = task_model.Task(**task_create.dict()) # Python 객체를 DB 모델로 변환
  db.add(task) 
  db.commit() # DB Commit
  db.refresh(task) # DB 데이터를 바탕으로 Task 인스턴스인 task를 업데이트 (DB에 작성된 레코드 ID 가져옴)
  return task

def get_task_with_done(db: Session) -> list[tuple[int, str, bool]]:
  result:Result = db.execute(
    select(
      task_model.Task.id,
      task_model.Task.title,
      task_model.Done.id.isnot(None).label("done"), # Done.id(o)->done=True, Done.id(x)->done=False
    ).outerjoin(task_model.Done)
  )
  return result.all()