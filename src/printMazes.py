from classes.Maze import Maze
from dummies.mazes import simple4r5cMaze, simple5r5cMaze
from src.classes.CellType import CellType

for cellType in CellType:
    print(cellType)

maze = Maze(simple5r5cMaze)

print('Total rows')
print(maze.totalRows)
print('Total columns')
print(maze.totalColumns)

maze.print()
