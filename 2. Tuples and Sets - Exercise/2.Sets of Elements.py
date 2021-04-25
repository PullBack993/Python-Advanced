num_n, num_m = [int(el) for el in input().split()]


set_n = set()
set_m = set()

for num in range(num_n):
    first_numbers = input()
    set_n.add(first_numbers)

for n in range(num_m):
    second_numbers = input()
    set_m.add(second_numbers)

intersec = set_n.intersection(set_m)

[print(i) for i in intersec]
