num = int(input())

uniq_el = set()

for n in range(num):
    chemi_el = input().split()
    for el in range(len(chemi_el)):
        uniq_el.add(chemi_el[el])

[print(el) for el in uniq_el]