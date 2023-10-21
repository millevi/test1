import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = created_at = Column(
        DateTime, default=lambda: datetime.datetime.now(), nullable=False
    )