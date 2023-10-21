from pydantic import BaseModel
import datetime

class QuestionCreate(BaseModel):
    questions_num: int

    class Config:
        orm_mode = True


class QuestionAdd(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True
