string = input()

stack = []
for char in string:
    stack.append(char)

result = ""
while stack:
    result += stack.pop()

print(result)

# or print(string[::-1])