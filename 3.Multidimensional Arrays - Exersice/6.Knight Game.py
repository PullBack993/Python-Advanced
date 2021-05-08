def is_valid_bound(row,col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def calculate_kills(mtrx, row,col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for i in range(len(rows)):
        potential_row = row+rows[i]
        potential_col = col+cols[i]
        if is_valid_bound(potential_row,potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == 'K':
                kills += 1
    return kills


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
removed_counter = 0
while True:
    max_kills = 0
    killer_position = []

    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == 'K':
                kills = calculate_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row_index, col_index]

    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        removed_counter += 1
    else:
        break

print(removed_counter)

