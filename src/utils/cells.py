from src.classes.CellType import CellType

cellTypeChar = {
    '#': CellType.WALL,
    'o': CellType.PLAYER,
    'x': CellType.EXIT,
    ' ': CellType.EMPTY,
}

DEFAULT_CELL_TYPE = CellType.WALL


def getCellTypeFromChar(char):
    return cellTypeChar[char] or DEFAULT_CELL_TYPE
