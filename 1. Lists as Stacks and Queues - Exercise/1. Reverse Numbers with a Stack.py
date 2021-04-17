from collections import deque
number = input().split()

q = deque([])

while number:
    q.append(number.pop())

print(" ".join(q))

