# input
# 2 4 6
# output
# The minimum number is 2
# The maximum number is 6
# The sum number is: 12

nums = list(map(int, input().split()))

print(f"The minimum number is {min(nums)}")
print(f"The maximum number is {max(nums)}")
print(f"The sum number is: {sum(nums)}")
