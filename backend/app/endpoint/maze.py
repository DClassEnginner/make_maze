from fastapi import APIRouter, HTTPException
from app.schemas import schemas
from app.modules.maze.maze import MazeType, make_maze

router = APIRouter()

@router.get("/", response_model=schemas.Maze)
async def get_maze(width: int = 10, height: int = 10, type: MazeType = MazeType.bar):
    if width < 5 or height < 5:
        raise HTTPException(status_code=400, detail="The width and height of the maze must be at least 5.")
    return make_maze(width, height, type)
