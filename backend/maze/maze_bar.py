from typing import List
from random import randint
from .maze_base import MazeBase

# 棒倒し法
class MazeBar(MazeBase):
    
    def create(self) -> List[List[int]]:

        self.maze[0][:] = [self.wall] * (self.width)
        self.maze[-1][:] = [self.wall] * (self.width)
        for x in self.maze:
            x[0] = self.wall
            x[-1] = self.wall
        
        for x in range(2, self.width - 1, 2):
            for y in range(2, self.height - 1, 2):
                self.maze[x][y] = self.wall
                
                while True:
                    direction = randint(0, 4) if y == 2 else randint(0, 3)
                    wallx = x
                    wally = y
                    if direction == 0: # 右
                        wallx += 1
                    elif direction == 1: # 下
                        wally += 1
                    elif direction == 2: # 左
                        wallx -= 1
                    else: #上
                        wally -= 1
                    
                    if self.maze[wallx][wally] != self.wall:
                        self.maze[wallx][wally] = self.wall
                        break
        
        return self.maze

if __name__ == '__main__':
    m = MazeBar()
    maze = m.create()
    print(maze)