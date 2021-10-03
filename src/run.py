from classes.Maze import Maze
from dummies.mazes import simple5r5cMaze, simple4r5cMaze, complexMaze
from src.classes.enums.CellType import CellType

maze1 = Maze(simple4r5cMaze)

maze1.run()

maze2 = Maze(simple5r5cMaze)

maze2.run()

maze3 = Maze(complexMaze)

maze3.run()
