from collections import deque
n = int(input())

station = deque([])

for _ in range(n):
    station.append([int(el) for el in input().split()])

tank_petrol = 0

for big_circle in range(n):
    is_valid = True
    tank_petrol = 0

    for small_circle in range(n):
        tank_petrol += int(station[small_circle][0]) - int(station[small_circle][1])

        if tank_petrol < 0:
            is_valid = False
            station.append(station.popleft())
            break

    if is_valid:
        print(big_circle)
        break