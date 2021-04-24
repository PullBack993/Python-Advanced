def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines

def print_result(names):
    [print(name) for name in names]


n = int(input())
names = input_to_list(n)
unique_names = set([name for name in names])
print_result(unique_names)