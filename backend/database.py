from sqlalchemy import create_engine, Column, Integer, String # type: ignore

from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

SQLALCHEMY_DATABASE_URL = "sqlite:///./viranora.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String, default="Beklemede")
    priority = Column(String, default="Orta")

Base.metadata.create_all(bind=engine)