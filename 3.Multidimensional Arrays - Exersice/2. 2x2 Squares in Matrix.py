def read_matrix():
    rows_count, columns_count = [int(x) for x in input().split()]
    matrix = []
    for _ in range(rows_count):
        row = input().split()
        matrix.append(row)
    return matrix


def check_el_equal(row, column, mtrx):
    current_el = mtrx[row][column]
    second_el = mtrx[row][column+1]
    el_bottom = mtrx[row+1][column]
    second_el_bottom = mtrx[row+1][column+1]
    if current_el == second_el and second_el == el_bottom and el_bottom == second_el_bottom:
        return True
    return False


def square_matrix(matrix):
    counter = 0
    row = len(matrix)
    col = len(matrix[0])
    for r in range(row - 1):
        for c in range(col-1):
            if check_el_equal(r, c, matrix):
                counter += 1

            """ or """
            # if m[r][c] == m[r][c + 1] == m[r + 1][c] == m[r + 1][c + 1]:
            #    counter += 1
    return counter


print(square_matrix(read_matrix()))