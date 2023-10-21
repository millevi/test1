from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db_models import Question as DBQuestion
from schemas import QuestionCreate
import requests
import json


async def get_question(db: AsyncSession) -> DBQuestion:
    query = (
        select(DBQuestion)
        .order_by(DBQuestion.created_at.desc())
    )
    result = await db.execute(query)
    return result.scalars().first() if result else None


async def add_question(db: AsyncSession, number:QuestionCreate):
    response = requests.get(f'https://jservice.io/api/random?count={number}')
    list_of_questions = json.loads(response.content)
    for q in list_of_questions:
        print(q)
        db_question = DBQuestion(
            id = q['id'],
            question = q['question'],
            answer = q['answer']
        )
        async with db.begin():
            db.add(db_question)
        await db.refresh(db_question)
        return db_question





