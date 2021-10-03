from src.classes.enums.CellType import CellType

cellTypeCharMap = {
    '#': CellType.WALL,
    'o': CellType.PLAYER,
    'x': CellType.EXIT,
    ' ': CellType.EMPTY,
}

DEFAULT_CELL_TYPE = CellType.WALL


def getCellTypeFromChar(char):
    return cellTypeCharMap[char] or DEFAULT_CELL_TYPE
