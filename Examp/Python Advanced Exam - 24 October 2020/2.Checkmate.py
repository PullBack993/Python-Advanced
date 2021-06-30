QUEEN = 'Q'
KING = 'K'
SIZE = 8

MOVES = [
    (1, 0),  # up
    (0, -1),  # left
    (-1, -1),  # up left
    (-1, 1),  # up right
    (0, 1),  # right
    (1, 1),  # down right
    (-1, 0),  # down
    (1, -1),  # down left
]


def get_input():
    return [input().split(' ') for _ in range(SIZE)]


def find_king(mtrx):
    for row_i in range(SIZE):
        for col_i in range(SIZE):
            if mtrx[row_i][col_i] == KING:
                return row_i, col_i


def is_valid(value):
    return 0 <= value < SIZE


def search_for_delta(mat, x, y, delta):
    move_x, move_y = delta
    while True:
        if not is_valid(x) or not is_valid(y):
            return
        if mat[x][y] == QUEEN:
            return [x, y]
        x += move_x
        y += move_y


def search_for_queens(mat, x, y):
    results = [search_for_delta(mat, x, y, move) for move in MOVES]
    return list(filter(lambda q: q, results))


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print('The king is safe!')


matrix = get_input()
position_x, position_y = find_king(matrix)
killer_queens = search_for_queens(matrix, position_x, position_y)
print_result(killer_queens)
