def is_stack(check_stack):
    if stack:
        return True
    return False


numbers = int(input())
stack = []
for n in range(numbers):
    command = input()
    if command.startswith("1"):
        number = command.split()
        element = int(number[1])
        stack.append(element)
    elif command.startswith("2") and is_stack(stack):
        stack.pop()
    elif command.startswith("3") and is_stack(stack):
        print(max(stack))
    elif command.startswith("4") and is_stack(stack):
        print(min(stack))

print(', '.join(map(str, stack[::-1])))