from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from database import SessionLocal, engine
from maze.maze import MazeType, make_maze
from backend import models, schemas
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)



app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/maze/", response_model=schemas.Maze)
async def get_maze(width: int = 10, height: int = 10, type: MazeType = MazeType.bar):
    if width < 5 and height < 5:
        raise HTTPException(status_code=400, detail="The width and height of the maze must be at least 5.")
    return make_maze(width, height, type)


@app.post("/score/")
async def get_maze(x: int = 10, y: int = 10, db: Session = Depends(get_db)):
    maze_list = []
    return maze_list