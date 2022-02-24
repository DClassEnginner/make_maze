from typing import List

from pydantic import BaseModel

class Maze(BaseModel):
    maze: List[List[int]]
    
    class Config:
        orm_mode = True