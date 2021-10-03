from enum import Enum


class CellType(Enum):
    WALL = '#'
    PLAYER = 'o'
    EXIT = 'x'
    EMPTY = ' '
