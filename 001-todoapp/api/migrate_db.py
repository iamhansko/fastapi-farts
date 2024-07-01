from sqlalchemy import create_engine

from api.models.task import Base

# 마이그레이션 작업은 자주 수행하거나 빠른 속도 요구하지 않으므로 비동기화 필요 X
# 굳이 aiomysql 사용하는 대신 pymysql 유지 
DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)

def reset_database():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)

if __name__=="__main__":
  reset_database()