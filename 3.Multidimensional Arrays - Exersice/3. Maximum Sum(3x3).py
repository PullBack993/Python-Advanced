def get_sum(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):

        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]

    return the_sum


rows_count, columns_count = [int(x) for x in input().split()]
matrix = []
best_sum = 0
current_sum = 0
best_row_index = 0
best_col_index = 0
SIZE = 3
for _ in range(rows_count):
    row = [int(el) for el in input().split()]
    matrix.append(row)


row = len(matrix)
col = len(matrix[0])
for r in range(row - 2):
    for c in range(col-2):
        current_sum = get_sum(matrix, r, c, SIZE)
        if current_sum > best_sum:
            best_sum = current_sum
            best_col_index = c
            best_row_index = r

print(f"Sum = {best_sum}")

for row in range(best_row_index, best_row_index + SIZE):
    el_matrix_size = []
    for col in range(best_col_index, best_col_index + SIZE):
        el_matrix_size.append(matrix[row][col])
    print(' '.join(str(x) for x in el_matrix_size))