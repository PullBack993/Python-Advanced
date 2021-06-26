import math


def read_matrix(r):
    matrix = [[x for x in input().split(" ")] for n in range(r)]
    return matrix


def is_valid_bound(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


n = int(input())
matrix = read_matrix(n)
position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            position = (row, col)
            matrix[row][col] = '0'
            break
    if position:
        break
curr_row, curr_col = position[0], position[1]

score = 0
path = []
winner = False
move = input()

while not winner:

    if move == "up":
        curr_row -= 1
    elif move == "down":
        curr_row += 1
    elif move == "left":
        curr_col -= 1
    elif move == "right":
        curr_col += 1
    else:
        move = input()
        continue

    if not is_valid_bound(curr_row, curr_col):
        break
    elif matrix[curr_row][curr_col] == "X":
        break

    else:
        score += int(matrix[curr_row][curr_col])
        path.append([curr_row, curr_col])
        if score >= 100:
            winner = True
            break

    move = input()

if not winner:
    score *= 0.5
    print(f"Game over! You've collected {math.floor(score)} coins.")
    print(f"Your path: ")
    print("\n".join([str(el) for el in path]))

else:
    print(f"You won! You've collected {score} coins.")
    print(f"Your path: ")
    print("\n".join([str(el) for el in path]))