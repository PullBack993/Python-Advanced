# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END

def check_index(row, col, mtrx):
    if 0 <= row < len(mtrx) and 0 <= col < len(mtrx):
        return True
    return False

def subtract(row, col, value, mtrx):
    if check_index(row, col, mtrx):
        mtrx[row][col] -= value
        return mtrx
    print(f"Invalid coordinates")
    return mtrx

def add(row, col, value, mtrx):
    if check_index(row, col, mtrx):
        mtrx[row][col] += value
        return mtrx
    print(f"Invalid coordinates")
    return mtrx


size_matrix = int(input())
matrix = []
[matrix.append([int(el) for el in input().split()]) for _ in range(size_matrix)]

data = input()
while not data == 'END':
    split_data = data.split()
    command = split_data[0]
    num_row = int(split_data[1])
    num_col = int(split_data[2])
    value = int(split_data[3])

    if command == 'Add':
        matrix = add(num_row, num_col, value, matrix)
    else:
        matrix = subtract(num_row, num_col, value, matrix)
    data = input()
[print(*el) for el in matrix]