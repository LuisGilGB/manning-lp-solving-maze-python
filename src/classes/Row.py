from src.classes.Cell import Cell
from src.classes.enums.CellType import CellType


class Row():
    def __init__(self, row_string):
        self.cells = []
        for cellChar in row_string:
            self.cells.append(Cell(cellChar))

    def print(self):
        row_string = ''
        for cell in self.cells:
            row_string += cell.to_string()
        print(row_string)

    def at(self, index):
        return self.cells[index]

    def has_player_at(self):
        try:
            for cell in self.cells:
                if cell.has_player():
                    return self.cells.index(cell)
            return False
        except:
            return False
