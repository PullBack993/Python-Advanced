def strongest_nums(numbers):
    sum_positive = sum(filter(lambda x: x > 0, numbers))
    sum_negative = sum(filter(lambda x: x < 0, numbers))
    print(sum_negative, sum_positive, sep="\n")
    if sum_positive > abs(sum_negative):
        print(f"The positives are stronger than the negatives")
    else:
        print(f"The negatives are stronger than the positives")

# Input
# 1 2 -3 -4 65 -98 12 57 -84
nums = [int(el) for el in input().split()]
strongest_nums(nums)

