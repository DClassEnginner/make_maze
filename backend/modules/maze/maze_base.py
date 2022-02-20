from enum import Enum
from typing import List
# import numpy as np

class MazeType(str, Enum):
    bar = "bar"
    extend = "extend"
    dig = "dig"

class MazeBase:
    
    path = 0
    wall = 1
    start = 2
    end = 3
    
    def __init__(self, width: int = 10, height: int = 10) -> None:
        self.width = width + 1 if (width % 2) == 0 else width
        self.height = height + 1 if (height % 2) == 0 else height
        # self.maze = np.zeros(self.width, self.height)
        self.maze = [[MazeBase.path] * (self.width) for i in range(self.height)]
    
    def create(self) -> List[int]:
        pass