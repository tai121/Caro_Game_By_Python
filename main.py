# This is a sample Python script.
import constants
from GameCaro import GameCaro


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = GameCaro()
    while True:
        board = game.get_board()
        for i in range(constants.SIZE_OF_BOARD):
            for j in range(constants.SIZE_OF_BOARD):
                print(board[i][j], end=' ')
            print()
        x, y = [int(x) for x in input("Enter two values: ").split()]
        result = game.move(x, y)
        if result == -1:
            print("Move again!!!")
        elif result == 0:
            continue
        else:
            print(result + " win!!!!!!!!!!!!!")
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
