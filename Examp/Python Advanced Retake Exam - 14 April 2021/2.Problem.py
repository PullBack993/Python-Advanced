import math


def check_index(r, c, max_index):
    if 0 <= r < max_index and 0 <= c < max_index:
        return True
    return False


def get_index(r, c, mtrx):
    most_left = int(mtrx[0][c])
    most_right = int(mtrx[-1][c])
    most_above = int(mtrx[r][0])
    most_below = int(mtrx[r][-1])
    sum_indexes = most_left + most_right + most_above + most_below
    return sum_indexes


def get_player(player):
    if player % 2 == 1:
        return True
    return False


def print_result(name, count_turns):
    print(f"{name} won the game with {count_turns} throws!")
    exit(0)


player_one, player_two = input().split(", ")
player_one_scour = 501
player_one_throws = 0
player_two_scour = 501
player_two_throws = 0
lines = 7
counter = 0
matrix = []
for _ in range(lines):
    matrix.append([el for el in input().split()])
    
row, col = input().split(", ")

while player_one_scour >= 0 or player_two_scour >= 0:
    row, col = int(row[1:]), int(col[:-1])
    counter += 1
    total = 0
    if check_index(row, col, lines):
        if matrix[row][col].isdigit():
            total = int(matrix[row][col])

        elif matrix[row][col] == 'D':
            total = get_index(row, col, matrix) * 2


        elif matrix[row][col] == 'T':
            total = get_index(row, col, matrix) * 3

        elif matrix[row][col] == 'B':
            if get_player(counter):
                print_result(player_one, (math.ceil(counter / 2)))
                exit(0)
            else:
                print_result(player_two, (math.ceil(counter / 2)))
                exit(0)

        if get_player(counter):
            player_one_scour -= total
            if player_one_scour <= 0:
                print_result(player_one, (math.ceil(counter / 2)))

        else:
            player_two_scour -= total
            if player_two_scour <= 0:
                print_result(player_two, (math.ceil(counter / 2)))
                break

    row, col = input().split(", ")
