from Grid import Grid
from enum import Enum, auto
import random

class HunterState(Enum):
    
    SEARCHING_PREY = auto()
    HUNTING_PREY = auto()

class Hunter():
    def __init__(self, initialX: int, initialY: int):
        self.x = initialX
        self.y = initialY
        self.element = 'W'
        self.state = HunterState.SEARCHING_PREY
        self.preyBeingHunted = None

    def move(self, grid: Grid):
        if(self.state == HunterState.SEARCHING_PREY):
            self.moveSearching(grid)
            self.preyBeingHunted = self.searchPrey(grid)
            if(self.preyBeingHunted != None):
                self.state = HunterState.HUNTING_PREY
        
        if(self.state == HunterState.HUNTING_PREY):
            self.moveHunting(grid)
        
    def searchPrey(self, grid: Grid, searchRange = 5):
        foundPrey = None
        for i in range(max(0, self.x - searchRange), min(grid.size - 1, self.x + searchRange)):
            for j in range(max(0, self.y - searchRange), min(grid.size - 1, self.y + searchRange)):
                if(grid.matrix[i][j] != 'X' and grid.matrix[i][j] != 'H'):
                    foundPrey = grid.matrix[i][j]
    
        return(foundPrey)
    
    
    def moveHunting(self, grid: Grid):
        preyPosition = self.preyPosition(grid)
        if(self.checkIfPreyIsClose(preyPosition)):
            grid.matrix[preyPosition[0]][preyPosition[1]] = 'X'
            self.state = HunterState.SEARCHING_PREY
        
        choice = [0, 0]
        if(self.x < preyPosition[0]):
            choice[0] += 1
        if(self.x > preyPosition[0]):
            choice[0] -= 1
        if(self.y < preyPosition[1]):
            choice[1] += 1
        if(self.y > preyPosition[1]):
            choice[1] -= 1
            
        if(
            (self.x + choice[0]) >= grid.size and
            (self.x + choice[0]) < 0
            ):
            choice[0] = 0
        
        if(
            (self.y + choice[1]) >= grid.size and
            (self.y + choice[1]) < 0
            ):
            choice[1] = 0
        
            
        grid.moveElementInMatrix(self.x, self.y, choice, self.element)
        self.x += choice[0]
        self.y += choice[1]
        
        if(self.checkIfPreyIsClose(preyPosition)):
            grid.matrix[preyPosition[0]][preyPosition[1]] = 'X'
            self.state = HunterState.SEARCHING_PREY
    
    
    def checkIfPreyIsClose(self, preyPosition):
        if(
            (abs(self.x - preyPosition[0]) <= 1 ) and
            (abs(self.y - preyPosition[1]) <= 1 )
        ):
            return(True)
        else:
            return(False)    

    def preyPosition(self, grid: Grid):
        for x, matrixI in enumerate(grid.matrix):
            for y, value in enumerate(matrixI):
                if value == self.preyBeingHunted:
                    return(x, y)

    
    def moveSearching(self, grid: Grid):
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
                if grid.emptySpace(self.x + choice[0], self.y + choice[1]):
                    moved = True
            
        grid.moveElementInMatrix(self.x, self.y, choice, self.element)
        self.x += choice[0]
        self.y += choice[1]
