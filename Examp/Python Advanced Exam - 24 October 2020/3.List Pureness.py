from collections import deque


def best_list_pureness(*args):
    list_number, n_times = args
    list_number = deque(list_number)
    best_sum = 0
    counter = 0
    save_best_rotation = 0

    for x in range(n_times + 1):
        total = 0
        for i in range(len(list_number)):
            total += list_number[i] * i
        if total > best_sum:
            best_sum = total
            save_best_rotation = counter
        counter += 1
        last = list_number.pop()
        list_number.appendleft(last)
    return \
        f"Best pureness {best_sum} after {save_best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
# test = ([7, 9, 2, 5, 3, 4], 3)
# test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
