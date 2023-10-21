from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from schemas import QuestionAdd, QuestionCreate
import crud

router = APIRouter()


@router.post("/question", response_model=QuestionAdd)
async def create_question(number: QuestionCreate, db: AsyncSession = Depends(get_async_session)):
    return await crud.add_question(db, number)