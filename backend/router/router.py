from fastapi import APIRouter
from endpoint import maze

router = APIRouter()
router.include_router(maze.router, prefix="/maze", tags=["maze"])

