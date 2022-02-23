from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db

router = APIRouter()

@router.post("/")
async def post_score(x: int = 10, y: int = 10, db: Session = Depends(get_db)):
    maze_list = []
    return maze_list
