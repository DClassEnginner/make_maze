from typing import List
from .maze_base import MazeType
from .maze_bar import MazeBar
from app.schemas import schemas



def make_maze(width: int = 10, height: int = 10, type: MazeType = MazeType.bar) -> schemas.Maze:
    
    maze = schemas.Maze
    if type == MazeType.bar:
        m = MazeBar(width, height)
        maze.maze = m.create()
    return maze
