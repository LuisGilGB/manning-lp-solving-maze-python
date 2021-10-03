from src.classes.Row import Row
from src.classes.enums.Direction import Direction
from src.utils.directions import side_check_order_by_direction_map


# This thing obviously need a refactor, but I'm tired and this is not production code, just a toy for learning purposes.
class Maze():
    def __init__(self, maze_string):
        aux_rows = maze_string.split('\n')
        self.rows = []
        self.playerPosition = ()
        for rawRow in aux_rows:
            row = Row(rawRow)
            self.rows.append(row)
            row_has_player_at = row.has_player_at()
            if row_has_player_at:
                row_index = len(self.rows) - 1
                self.playerPosition = (row_index, row_has_player_at)
        self.currentDirection = self.get_starting_direction()
        print('Maze:')
        self.print()
        print()

    def print(self):
        for row in self.rows:
            row.print()

    def print_player_position(self):
        print('Player at:', self.playerPosition)

    def get_cell_at(self, row_index, col_index):
        return self.rows[row_index].at(col_index)

    def get_player_cell(self):
        return self.get_cell_at(self.playerPosition[0], self.playerPosition[1])

    def get_starting_direction(self):
        player_row = self.playerPosition[0]
        player_col = self.playerPosition[1]
        result = Direction.TOP
        if self.get_cell_at(player_row - 1, player_col).is_wall():
            result = Direction.LEFT
        if self.get_cell_at(player_row, player_col - 1).is_wall():
            result = Direction.BOTTOM
        if self.get_cell_at(player_row + 1, player_col).is_wall():
            result = Direction.RIGHT
        return result

    def get_next_player_position(self, direction):
        if direction == Direction.TOP:
            return (self.playerPosition[0] - 1, self.playerPosition[1])
        if direction == Direction.BOTTOM:
            return (self.playerPosition[0] + 1, self.playerPosition[1])
        if direction == Direction.LEFT:
            return (self.playerPosition[0], self.playerPosition[1] - 1)
        if direction == Direction.RIGHT:
            return (self.playerPosition[0], self.playerPosition[1] + 1)
        return self.playerPosition

    def calculate_direction_for_next_step(self):
        checks_order = side_check_order_by_direction_map[self.currentDirection]
        for direction in checks_order:
            draft_position = self.get_next_player_position(direction)
            if self.get_cell_at(draft_position[0], draft_position[1]).is_valid_for_advance():
                return direction
        return self.currentDirection

    def advance(self):
        # print('--- MOVE START ---')
        direction_for_next_step = self.calculate_direction_for_next_step()
        self.playerPosition = self.get_next_player_position((direction_for_next_step))
        print('Player goes to', self.playerPosition)
        self.currentDirection = direction_for_next_step
        print('Player is facing', self.currentDirection)
        return False
        # print('---- MOVE END ----')

    def run(self):
        print('Let\'s start')
        self.print_player_position()
        print('Starts going to:', self.currentDirection)
        result = self.get_player_cell().is_exit()
        while not result:
            self.advance()
            result = self.get_player_cell().is_exit()
        print('WE REACH THE EXIT!!!')
