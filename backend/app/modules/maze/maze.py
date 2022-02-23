from typing import List
from .maze_base import MazeType
from .maze_bar import MazeBar
from schemas import schemas



def make_maze(width: int = 10, height: int = 10, type: MazeType = MazeType.bar) -> schemas.Maze:
    
    maze = schemas.Maze
    if type == MazeType.bar:
        m = MazeBar(width, height)
    elif type == MazeType.extend:
        m = make_maze_extend(width, height)
    else:
        m = make_maze_dig(width, height)
    
    maze.maze = m.create()
    return maze


def make_maze_extend(width: int = 10, height: int = 10) -> List[int]:
    pass

def make_maze_dig(width: int = 10, height: int = 10) -> List[int]:
    pass