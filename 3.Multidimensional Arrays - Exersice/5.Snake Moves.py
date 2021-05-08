rows, columns = [int(el) for el in input().split()]
matrix = []
word = input()
index_word = 0

for row_index in range(rows):
    matrix.append([0 for el in range(columns)])

for row_index in range(rows):
    for col_index in range(columns):
        matrix[row_index][col_index] = word[index_word]
        index_word += 1
        if index_word == len(word):
            index_word = 0

for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print("".join(str(el) for el in matrix[row_index]))