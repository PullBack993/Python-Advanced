def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['X', '!', '@'],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            matrix.append(list(input()))

        return matrix


def get_symbol(matrix):
    symbol = input()
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if symbol == matrix[r][c]:
                return r, c
    return f"{symbol} does not occur in the matrix"


print(get_symbol(read_matrix()))
