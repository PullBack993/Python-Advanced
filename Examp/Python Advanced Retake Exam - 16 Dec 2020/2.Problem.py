def read_matrix(r):
    mtrx = [[x for x in input()] for n in range(r)]
    return mtrx


def is_valid_bound(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


word = str(input())
size_matrix = int(input())
matrix = read_matrix(size_matrix)

position = None

for row in range(size_matrix):
    for col in range(size_matrix):
        if matrix[row][col] == 'P':
            position = (row, col)
            break
    if position:
        break
curr_row, curr_col = position[0], position[1]

move_steps = int(input())

while move_steps > 0:
    move_command = input()
    move_steps -= 1
    old_position_r = curr_row
    old_position_c = curr_col

    if move_command == "up":
        curr_row -= 1
    elif move_command == "down":
        curr_row += 1
    elif move_command == "left":
        curr_col -= 1
    elif move_command == "right":
        curr_col += 1
    else:
        continue

    if not is_valid_bound(curr_row, curr_col, size_matrix):
        if word:
            word = word[:-1]
            if move_command == "up":
                curr_row += 1
            elif move_command == "down":
                curr_row -= 1
            elif move_command == "left":
                curr_col += 1
            elif move_command == "right":
                curr_col -= 1
            else:
                move_command = input()
                continue
        continue
    elif matrix[curr_row][curr_col].isalpha():
        word += str(matrix[curr_row][curr_col])
        matrix[old_position_r][old_position_c] = '-'
        matrix[curr_row][curr_col] = 'P'
    else:
        matrix[curr_row][curr_col] = 'P'
        matrix[old_position_r][old_position_c] = '-'

print(word)
for el in matrix:
    print(''.join(el))