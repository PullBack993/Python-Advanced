FOOD = '*'
SNAKE = 'S'
BURROWS = 'B'
MOVE_SYMBOL = '.'
MAX_FOOD = 9


def get_input(size):
    board = []
    for _ in range(size):
        board.append([el for el in input()])
    return board


def find_snake(board, size):
    for row_i in range(size):
        for col_i in range(size):
            if board[row_i][col_i] == SNAKE:
                return row_i, col_i


def find_burrows(board):
    for row_i in range(len(board)):
        for col_i in range(len(board)):
            if board[row_i][col_i] == BURROWS:
                return row_i, col_i


def check_index(mat, r, c):
    size_matrix = len(mat)
    if 0 <= r < size_matrix and 0 <= c < size_matrix:
        return True
    return False


size = int(input())
board = get_input(size)
snake_row, snake_col = find_snake(board, size)
food = 0
game_over = False
while not game_over and MAX_FOOD >= food:
    move_command = input()
    old_row_position = snake_row
    old_col_position = snake_col
    if move_command == "up":
        snake_row -= 1
    elif move_command == "down":
        snake_row += 1
    elif move_command == "left":
        snake_col -= 1
    elif move_command == "right":
        snake_col += 1

    position = check_index(board, snake_row, snake_col)
    if position:
        new_row = snake_row
        new_col = snake_col
        new_position = board[new_row][new_col]
        if new_position == FOOD:
            food += 1
            board[old_row_position][old_col_position] = MOVE_SYMBOL
            board[new_row][new_col] = SNAKE
        elif new_position == BURROWS:
            board[old_row_position][old_col_position] = MOVE_SYMBOL
            board[new_row][new_col] = MOVE_SYMBOL
            row, col = find_burrows(board)
            snake_row, snake_col = row, col
            board[row][col] = SNAKE
        else:
            board[old_row_position][old_col_position] = MOVE_SYMBOL
            board[new_row][new_col] = SNAKE

    else:
        board[old_row_position][old_col_position] = MOVE_SYMBOL
        game_over = True

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")

for el in board:
    print("".join(i for i in el))
