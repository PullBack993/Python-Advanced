# input
# Odd
# 1 3 5 34 7 9 12 11 13 10

def even_or_odd(command, nums):
    if command == 'Odd':
        sum_odd = sum([el for el in nums if el % 2 == 1])
        print(sum_odd * len(nums))
    else:
        sum_even = sum([el for el in nums if el % 2 == 0])
        print(sum_even * len(nums))


data = input()
numbers = [int(el) for el in input().split()]
even_or_odd(data, numbers)
