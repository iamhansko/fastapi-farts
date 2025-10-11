from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model

async def get_done(db:AsyncSession, task_id:int) -> task_model.Done | None:
  result:Result = await db.execute(
    select(task_model.Done).filter(task_model.Done.id == task_id)
  )
  return result.scalars().first()

async def create_done(db:AsyncSession, task_id:int) -> task_model.Done:
  done = task_model.Done(id=task_id)
  db.add(done)
  await db.commit() # DB Commit
  await db.refresh(done) # DB 데이터를 바탕으로 Done 인스턴스인 done 업데이트 (DB에 작성된 레코드 ID 가져옴)
  return done

async def delete_done(db:AsyncSession, original:task_model.Done) -> None:
  await db.delete(original)
  await db.commit()