from random import sample


def getInt(massage: str, start: int, end: int):
    while True:
        try:
            num = int(input(massage))
            if start <= num:
                if num <= end or end == 0:
                    break
        except ValueError:
            pass
    return num


def print2d(array):
    for i in range(len(array)):
        print()
        for j in range(len(array[0])):
            print(array[i][j], end="\t")
    print()


height = getInt("input the height : ", 0, 0)
width = getInt("input the width : ", 0, 0)
bombs = getInt("how many bombs ?  ", 0, (width * height))
game = [[0] * width for _ in range(height)]
shuffle = sample([i for i in range(width * height)], bombs)
print(shuffle)
for i in shuffle:
    game[i // width][i % width] = 9
print2d(game)
for i in range(height):
    for j in range(width):
        if game[i][j] == 0:
            counter = 0
            for y in range(i - 1, i + 2):
                for x in range(j - 1, j + 2):
                    if 0 <= y < height and 0 <= x < width:
                        if game[y][x] == 9:
                            counter += 1
            game[i][j] = counter
print2d(game)
board = [["?"] * width for _ in range(height)]
print2d(board)


def clearEmpty(i, j):
    for y in range(i - 1, i + 2):
        for x in range(j - 1, j + 2):
            if 0 <= y < height and 0 <= x < width:
                if game[y][x] == 0:
                    board[y][x] = " "
                    game[y][x] = 10
                    clearEmpty(y, x)
                elif game[y][x] < 9:
                    board[y][x] = game[y][x]
                    game[y][x] = 10


def checkAll():
    for i in range(height):
        for j in range(width):
            if game[i][j] < 9:
                return False
    return True


def choosing():
    x = getInt("choose colum : ", 1, width) - 1
    y = getInt("choose row : ", 1, height) - 1
    if game[y][x] == 9:
        board[y][x] = "X"
        game[y][x] = 10
        print2d(board)
        print("\n\nYou lost")
        return
    elif game[y][x] == 0:
        clearEmpty(y, x)
    elif game[y][x] == 10:
        print("\n\nAlready chosen")
    else:
        board[y][x] = game[y][x]
        game[y][x] = 10
    print2d(board)
    if checkAll():
        print("\n\nYou Won")
        return
    choosing()

choosing()