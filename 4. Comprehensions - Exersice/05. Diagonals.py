# input
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
def sec_diagonal(mtrx, size):
    return [second_diagonal.append(mtrx[i][size - i - 1]) for i in range(len(mtrx))]

def fir_diagonal(mtrx):
    return [first_diagonal.append(mtrx[i][i]) for i in range(len(mtrx))]


size_matrix = int(input())
matrix = []
[matrix.append([int(el) for el in input().split(', ')]) for _ in range(size_matrix)]
"""or"""
# for _ in range(size_matrix):
#     matrix.append([int(el) for el in input().split(', ')])

first_diagonal = []
second_diagonal = []
fir_diagonal(matrix)
sec_diagonal(matrix, size_matrix)

print(f"First diagonal: {', '.join(repr(e) for e in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(repr(e) for e in second_diagonal)}. Sum: {sum(second_diagonal)}")

