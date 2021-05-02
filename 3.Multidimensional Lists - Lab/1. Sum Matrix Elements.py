rows, columns = input().split(", ")
rows = int(rows)
columns = int(columns)
# rows, columns = [int(x) for x in input(", ")]
sum_matrix = 0
matrix = []

for row in range(rows):
    matrix.append(list(int(x) for x in input().split(", ")))
    for column in range(columns):
        sum_matrix += matrix[row][column]

print(sum_matrix)
print(matrix)