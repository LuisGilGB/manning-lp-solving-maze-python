from src.utils.cells import getCellTypeFromChar


class Cell():
    def __init__(self, cellChar):
        self.cellType = getCellTypeFromChar(cellChar)

    def print(self):
        print(self.cellType.value)

    def toString(self):
        return self.cellType.value
