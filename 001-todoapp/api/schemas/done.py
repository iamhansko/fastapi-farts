from pydantic import BaseModel

class DoneResponse(BaseModel):
  id: int
  class Config:
    orm_mode=True # 암묵적으로 ORM에서 DB 모델의 객체를 받아들여 응답 스키마로 변환