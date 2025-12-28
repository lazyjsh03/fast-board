from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends
from app.core.config import settings
from typing import Generator

# 데이터베이스 연결 엔진 생성
engine = create_engine(settings.DATABASE_URL, echo=True)


# 테이블 생성 함수
def init_db():
    SQLModel.metadata.create_all(engine)


# FastAPI Dependency: 요청마다 새로운 DB 세션을 생성하고 종료함
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
