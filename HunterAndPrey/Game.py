from Prey import Prey
from Hunter import Hunter
from Grid import Grid
from random import randint
from time import sleep
import os

def PreyExists(grid: Grid, prey: str):
    found = False
    
    for x, matrixI in enumerate(grid.matrix):
        for y, value in enumerate(matrixI):
            if value == prey:
                found = True

    return(found)

def printGrid(grid: Grid):
    os.system('cls')
    grid.printMatrix()

if __name__ == "__main__":
    numberOfPreys = randint(5, 9)
    grid = Grid(7)
    
    hunter = Hunter(randint(0, grid.size - 1), randint(0, grid.size - 1))
    grid.insertElementInMatrix(hunter.x, hunter.y, hunter.element)
    listOfPreys = []
    for i in range(numberOfPreys):
        listOfPreys.append(
            Prey(randint(0, grid.size - 1), randint(0, grid.size - 1), str(i))
        )
        prey = listOfPreys[-1]
        grid.insertElementInMatrix(prey.x, prey.y, prey.preyID)
    
    printGrid(grid)
    sleep(1)

    while(len(listOfPreys) > 0):
        i+= 1
        for prey in listOfPreys:
            prey.move(grid)
        
        hunter.move(grid)
        
        for prey in listOfPreys:
            if not PreyExists(grid, prey.preyID):
                listOfPreys.remove(prey)
                
        printGrid(grid)
        sleep(1)
