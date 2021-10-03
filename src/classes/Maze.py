from src.classes.Row import Row


class Maze():
    def __init__(self, mazeString):
        auxRows = mazeString.split('\n')
        rows = []
        for row in auxRows:
            rows.append(Row(row))
        self.rows = rows
        self.totalRows = len(auxRows)
        self.totalColumns = len(auxRows[0])

    def print(self):
        for row in self.rows:
            row.print()
