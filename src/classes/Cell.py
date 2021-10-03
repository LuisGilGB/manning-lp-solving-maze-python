from src.classes.enums.CellType import CellType
from src.utils.cells import getCellTypeFromChar


class Cell():
    def __init__(self, cell_char):
        self.cellType = getCellTypeFromChar(cell_char)

    def print(self):
        print(self.cellType.value)

    def to_string(self):
        return self.cellType.value

    def has_player(self):
        return self.cellType == CellType.PLAYER

    def is_wall(self):
        return self.cellType == CellType.WALL

    def is_exit(self):
        return self.cellType == CellType.EXIT

    def is_empty(self):
        return self.cellType == CellType.EMPTY

    def is_valid_for_advance(self):
        return not self.is_wall()
