num = int(input())
names = set()

for n in range(num):
    name = input()
    names.add(name)

for name in names:
    print(name)