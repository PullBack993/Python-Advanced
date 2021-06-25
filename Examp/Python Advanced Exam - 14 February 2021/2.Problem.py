import math


def check_position(row, col, matrix):
    if matrix[row][col] == 'X':
        return False
    return True


def check_index(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def print_game_over(coins, positions):
    print(f"Game over! You've collected {math.floor(coins / 2)} coins.")
    print("Your path:")
    for el in range(len(positions)):
        print(positions[el])
    exit()


field_size = int(input())
matrix = []
for _ in range(field_size):
    matrix.append([el for el in input().split(' ')])

player_position_row = 0
player_position_col = 0
PLAYER = "P"
for row in range(len(matrix)):
    if PLAYER in matrix[row]:
        col = matrix[row].index(PLAYER)
        player_position_row = row
        player_position_col = col

coins = 0
position = []
while not coins >= 100:
    command = input()
    if command == 'up':
        if check_index(player_position_row - 1, player_position_col, field_size) \
                and check_position(player_position_row - 1, player_position_col, matrix):

            player_position_row -= 1
            coins += int(matrix[player_position_row][player_position_col])
            new_position = [player_position_row, player_position_col]
            position.append(new_position)
        else:
            print_game_over(coins, position)

    elif command == 'down':
        if check_index(player_position_row + 1, player_position_col, field_size) \
                and check_position(player_position_row + 1, player_position_col, matrix):
            player_position_row += 1
            coins += int(matrix[player_position_row][player_position_col])
            new_position = [player_position_row, player_position_col]
            position.append(new_position)
        else:
            print_game_over(coins, position)

    elif command == 'left':
        if check_index(player_position_row, player_position_col - 1, field_size) \
                and check_position(player_position_row, player_position_col - 1, matrix):
            player_position_col -= 1
            coins += int(matrix[player_position_row][player_position_col])
            new_position = [player_position_row, player_position_col]
            position.append(new_position)
        else:
            print_game_over(coins, position)

    elif command == 'right':
        if check_index(player_position_row, player_position_col + 1, field_size) \
                and check_position(player_position_row, player_position_col + 1, matrix):
            player_position_col += 1
            coins += int(matrix[player_position_row][player_position_col])
            new_position = [player_position_row, player_position_col]
            position.append(new_position)
        else:
            print_game_over(coins, position)

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
    print("Your path:")
    for el in range(len(position)):
        print(position[el])
