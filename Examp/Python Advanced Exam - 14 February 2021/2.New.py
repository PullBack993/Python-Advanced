PLAYER = "P"
WALL = "X"

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def read_input():
    size = int(input())
    return [input().split(' ') for _ in range(size)]


def find_player(matrix, player):
    for row in range(len(matrix)):
        if player in matrix[row]:
            col = matrix[row].index(player)
            return row, col


def move_player(board, n_r, n_c, position_player):
    pl_row, pl_col = position_player
    new_player_row = pl_row + n_r
    new_player_col = pl_col + n_c
    if check_index(new_player_row, new_player_col, len(board)):
        return False
    return new_player_row, new_player_col


def check_move(board, new_r, new_c):
    new_cell = board[new_r][new_c]
    if new_cell == WALL:
        return False
    return True


def collect_coins(board, new_x, new_y):
    coins = int(board[new_x][new_y])
    return coins


def check_coin(coins, path):
    if coins >= 100:
        print_win(coins, path)


def check_index(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return False
    return True


def print_win(coins, path):
    print(f'You won! You\'ve collected {coins} coins.')
    print_path(path)
    exit()


def print_game_over(coins, path):
    print(f'Game over! You\'ve collected {coins // 2} coins.')
    print_path(path)
    exit()


def print_path(moves):
    print('Your path:')
    [print([x , y]) for x, y in moves]


board = read_input()
player_row, player_col = find_player(board, PLAYER)
player = player_row, player_col
coins = 0
positions = []

while True:
    command = input()
    if command not in DIRECTIONS.keys():
        continue
    next_row, next_col = DIRECTIONS[command]
    player_position = move_player(board, next_row, next_col, player)
    if player_position:
        new_row, new_col = player_position
        if check_move(board, new_row, new_col):
            coins += collect_coins(board, new_row, new_col)
            player = new_row, new_col
            positions.append(player)
            check_coin(coins, positions)
        else:
            game_over = print_game_over(coins, positions)
    else:
        game_over = print_game_over(coins, positions)
