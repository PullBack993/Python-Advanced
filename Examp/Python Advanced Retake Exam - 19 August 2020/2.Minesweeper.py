EMPTY_CELL = ' '
MINE_CELL = '*'
NEIGHBOUR_CELLS_DISTANCE = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def get_matrix(size):
    matrix = [[' ' for _ in range(size)] for _ in range(size)]
    return matrix


def set_bomb(n, matrix):
    for el in range(n):
        first_n, second_n = input().split(", ")
        x, y = first_n[1:], second_n[:-1]
        matrix[int(x)][int(y)] = '*'
    return matrix


def is_valid_bound(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def check_for_bombs(mtrx, row, col):
    bombs_counter = 0
    for neighbour in NEIGHBOUR_CELLS_DISTANCE:
        row_i, col_i = neighbour
        row_move = row_i + row
        col_move = col_i + col
        if is_valid_bound(row_move, col_move, len(mtrx)):
            if matrix[row_move][col_move] == MINE_CELL:
                bombs_counter += 1
    return bombs_counter


matrix = get_matrix(int(input()))
count_bomb = int(input())
bomb = set_bomb(count_bomb, matrix)

for row_index in range(len(matrix)):
    for col_index in range(len(matrix)):
        if matrix[row_index][col_index] == EMPTY_CELL:
            mine = check_for_bombs(matrix, row_index, col_index)
            matrix[row_index][col_index] = mine

for r in range(len(matrix)):
    print(' '.join(map(str, matrix[r])))
