from typing import List
from maze_base import MazeBase

# 壁伸ばし法
class MazeExtend(MazeBase):
    
    def create(self) -> List[int]:
        
        maze = []
        for y in self.height:
            mz = []
            for x in self.width:
                m = super.path
                if x == 0 and y == 0 and x == self.width - 1 and y == self.height - 1:
                    m = super.wall
                mz.append(m)
            maze.append(mz)
        
        self.dig(1, 1)
        
        for y in self.height:
            for x in self.width:
                if x == 0 and y == 0 and x == self.width - 1 and y == self.height - 1:
                    maze[x][y] = super.wall
        
        return maze
    
    def dig(self, x, y) -> None:
        
        while True:
            