# Input 4 6

row, column = [int(el) for el in input().split()]

result = [[f"{chr(r)}{chr(c)}{chr(r)}" for c in range(r, r+column)]for r in range(97, 97+row)]
print(*[' '.join(i) for i in result], sep='\n')


"""or"""

# matrix_palindromes = []
#
# for r in range(97, 97+row):
#     matrix_palindromes = []
#     for c in range(r, r+column):
#         matrix_palindromes.append(chr(r)+chr(c)+chr(r))
#     print(*[''.join(i) for i in matrix_palindromes], end='\n')


