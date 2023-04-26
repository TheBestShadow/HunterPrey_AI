from Grid import Grid
import random

class Prey():
    def __init__(self, initialX: int, initialY: int, preyID: str):
        self.x = initialX
        self.y = initialY
        self.preyID = preyID
        
        
    def move(self, grid: Grid):
        
        moved = False
        
        while not moved:
            allOptions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, 1), 
                (1, 0),
                (1, -1)
            ]
            
            try:
                if self.x == 0:
                    allOptions.remove((-1, -1))
                    allOptions.remove((-1, -0))
                    allOptions.remove((-1, 1))
                    
                
                if self.x == grid.size - 1:
                    allOptions.remove((1, 0))
                    allOptions.remove((1, 1))
                    allOptions.remove((1, -1))

                if self.y == 0:
                    allOptions.remove((-1, -1))
                    allOptions.remove((0, -1))
                    allOptions.remove((1, -1))
                    
                
                if self.y == grid.size - 1:
                    allOptions.remove((0, 1))
                    allOptions.remove((-1, 1))
                    allOptions.remove((1, 1))
            
            except ValueError:
                pass
        
            choice = random.choice(allOptions)
            

            if( (self.x + choice[0] < grid.size) and
                (self.y + choice[1] < grid.size) and
                (self.x + choice[0] >= 0) and
                (self.x + choice[1] >= 0)):
                if (grid.emptySpace(self.x + choice[0], self.y + choice[1])):
                    moved = True
            
        grid.moveElementInMatrix(self.x, self.y, choice, self.preyID)
        self.x += choice[0]
        self.y += choice[1]
                    
if __name__ == "__main__":
    
    grid = Grid(5)
    prey1 = Prey(4, 4, 1)
    grid.insertElementInMatrix(prey1.x, prey1.y, prey1.preyID)
    grid.printMatrix()    
    
    print()
    prey1.move(grid)
    grid.printMatrix()