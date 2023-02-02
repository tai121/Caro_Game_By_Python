import constants


class GameCaro:
    def __init__(self):
        self.board = list(list(constants.DEFAULT_MOVE for _ in range(constants.SIZE_OF_BOARD)) for _ in range(
            constants.SIZE_OF_BOARD))
        self.__moving = 0

    def __check_direction(self, x_axis, y_axis, x_step, y_step, this_point):
        value = 0
        for i in range(1, 5):
            x = x_axis + x_step * i
            y = y_axis + y_step * i
            if x < 0 or y < 0 or x >= constants.SIZE_OF_BOARD or y > constants.SIZE_OF_BOARD or self.board[x][y] != \
                    this_point:
                return value
            value += 1
        return value

    def move(self, x_axis, y_axis):
        if x_axis < 0 or x_axis >= constants.SIZE_OF_BOARD or y_axis < 0 or y_axis >= constants.SIZE_OF_BOARD or \
                self.board[x_axis][y_axis] != constants.DEFAULT_MOVE:
            return -1
        this_point = constants.MOVING[self.__moving % 2]
        self.board[x_axis][y_axis] = this_point
        self.__moving += 1
        for i in range(-1, 2):
            for j in range(i + 1, 2):
                if self.__check_direction(x_axis, y_axis, i, j, this_point) + self.__check_direction(x_axis,
                                                                                                     y_axis, i * -1,
                                                                                                     j * -1,
                                                                                                     this_point) >= 4:
                    return this_point
        if self.__check_direction(x_axis, y_axis, 1, 1, this_point) + self.__check_direction(x_axis, y_axis, -1, -1,
                                                                                             this_point) >= 4:
            return this_point
        return 0

    def get_board(self):
        return self.board
