MIN_X = 1
MAX_X = 109
PUSH_QUERY = "1"
DEL_QUERY = "2"
MAX_QUERY = "3"
MIN_QUERY = "4"

stack = []

len_queries = int(input())

for _ in range(len_queries):
    command = input().split()
    query = command[0]
    if query == PUSH_QUERY:
        element = int(command[1])
        stack.append(element)
    elif query == DEL_QUERY:
        if stack:
            stack.pop()
    elif query == MAX_QUERY:
        if stack:
            max_stack = stack.copy()
            maximum = MIN_X
            while max_stack:
                el = max_stack.pop()
                if el >= maximum:
                    maximum = el
            print(maximum)
    elif query == MIN_QUERY:
        if stack:
            min_stack = stack.copy()
            minimum = MAX_X
            while min_stack:
                el = min_stack.pop()
                if el <= minimum:
                    minimum = el
            print(minimum)

output = []
while stack:
    output.append(stack.pop())

print(', '.join(map(str, output)))
