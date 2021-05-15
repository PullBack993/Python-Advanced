# input
# 1 2 3 4

def filter_even(i):
    return list(filter(lambda x: x % 2 == 0, i))


numbers = map(int, input().split())
print(filter_even(numbers))