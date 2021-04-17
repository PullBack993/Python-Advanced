from collections import deque

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'

names_deque = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{len(names_deque)} people remaining.')
        break
    elif command == PAID_COMMAND:
        while names_deque:
            print(names_deque.popleft())
    else:
        names_deque.append(command)