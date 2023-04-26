class Grid():
    def __init__(self, size: int):
        self.size = size
        self.matrix = []
        
        for _ in range(size):
            newLineMatrix = ['X' for _ in range(size)]
            self.matrix.append(newLineMatrix)
        
    def emptySpace(self, x, y):
        if(self.matrix[x][y] == 'X'):
            return(True)
        else:
            return(False)
        
    def insertElementInMatrix(self, x, y, element):
        self.matrix[x][y] = element
        
    def moveElementInMatrix(self, x, y, movement, element):
        self.matrix[x][y] = 'X'
        self.matrix[x+movement[0]][y+movement[1]] = element
        
    def printMatrix(self):
        print('\n'.join(['  '.join([str(cell) for cell in row]) for row in self.matrix]))
        
if __name__ == "__main__":
    grid = Grid(30)
    grid.printMatrix()