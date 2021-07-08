def numbers_searching(*args):
    numbers = sorted(args)
    duplicate_el = []
    need_el = set()
    set_el = set()
    is_found = False
    for el in range(len(numbers)):
        if numbers[el] + 1 not in numbers and not is_found:
            need_el.add(numbers[el] + 1)
            is_found = True

        if numbers[el] in set_el and numbers[el] not in duplicate_el:
            duplicate_el.append(numbers[el])
        set_el.add(numbers[el])
    need_el = list(need_el)
    need_el.append(duplicate_el)
    return need_el


print(numbers_searching(1, 2, 4, 2, 5, 4))  # Output [3, [2, 4]]
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))  # Output[6, [5, 7, 9]]
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))  # Output[46, [44, 45, 47, 48, 50]]
