# Input
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
nums = [int(el) for el in input().split(", ")]
positive = []
negative = []
even = []
odd = []

for num in nums:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"Positive: {', '.join(repr(e) for e in positive)}")
print(f"Negative: {', '.join(repr(e) for e in negative)}")
print(f"Even: {', '.join(repr(e) for e in even)}")
print(f"Odd: {', '.join(repr(e) for e in odd)}")

