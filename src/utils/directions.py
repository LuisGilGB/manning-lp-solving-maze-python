from src.classes.enums.Direction import Direction

side_check_order_by_direction_map = {
    Direction.TOP: (Direction.RIGHT, Direction.TOP, Direction.LEFT, Direction.BOTTOM),
    Direction.LEFT: (Direction.TOP, Direction.LEFT, Direction.BOTTOM, Direction.RIGHT),
    Direction.BOTTOM: (Direction.LEFT, Direction.BOTTOM, Direction.RIGHT, Direction.TOP),
    Direction.RIGHT: (Direction.BOTTOM, Direction.RIGHT, Direction.TOP, Direction.LEFT)
}