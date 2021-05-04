def read_matrix():
    size_matrix = int(input())
    matrix = []
    for _ in range(size_matrix):
        matrix.append([int(el) for el in input().split()])
    return matrix


def sum_primary_diagonal(mtx):
    primary_diagonal = 0
    for i in range(len(matrix)):
        primary_diagonal += matrix[i][i]
    return primary_diagonal

def sum_secondary_diagonal(mtx):
    secondary_diagonal = 0
    size = len(matrix)
    for i in range(size):
        secondary_diagonal += matrix[i][size - i - 1]
    return secondary_diagonal

def print_result(pr_d, sec_d):
    print(abs(pr_d - sec_d))


matrix = read_matrix()
primary_d = sum_primary_diagonal(matrix)
secondary_d = sum_secondary_diagonal(matrix)
print_result(primary_d, secondary_d)