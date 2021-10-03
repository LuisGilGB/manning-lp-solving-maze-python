from src.classes.Cell import Cell


class Row():
    def __init__(self, rowString):
        self.cells = []
        for cellChar in rowString:
            self.cells.append(Cell(cellChar))

    def print(self):
        rowString = ''
        for cell in self.cells:
            rowString += cell.toString()
        print(rowString)
