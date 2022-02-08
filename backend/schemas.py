from typing import List

from pydantic import BaseModel

class Score(BaseModel):
    name: str
    type: str
    x: int
    y: int
    score: int
    
    class Config:
        orm_mode = True

class Maze(BaseModel):
    maze: List[List[int]]
    
    class Config:
        orm_mode = True