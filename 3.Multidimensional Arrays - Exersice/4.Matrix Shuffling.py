def check_index(index, mtrx):
    index = list(map(int, index))
    for n in range(len(index)):
        if index[n] > len(mtrx):
            return True
    return False


def swap_element(index, mtrx):
    first_row, first_col, second_row, second_col = index
    first_row = int(first_row)
    first_col = int(first_col)
    second_col = int(second_col)
    second_row = int(second_row)
    mtrx[first_row][first_col], mtrx[second_row][second_col] = \
        mtrx[second_row][second_col], mtrx[first_row][first_col]
    return mtrx

def print_matrix(m):
    for row in range(len(m)):
        print(" ".join(map(str, m[row])))

rows_count, columns_count = [int(x) for x in input().split()]
matrix = []
for _ in range(rows_count):
    row = input().split()
    matrix.append(row)

data = input()
while not data == 'END':
    command, *swap_index = data.split()
    if len(swap_index) < 4 or len(swap_index) > 4 or check_index(swap_index, matrix):
        print('Invalid input!')
    elif command == 'swap':
        print_matrix(swap_element(swap_index, matrix))
    data = input()