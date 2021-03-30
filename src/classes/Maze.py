class Maze():
    def __init__(self, mazeString):
        auxRows = mazeString.split('\n')
        self.totalRows = len(auxRows)
        self.totalColumns = len(auxRows[0])
