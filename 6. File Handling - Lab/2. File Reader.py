text_file = open('2.numbers.txt', 'r')
nums_sum = 0
for num in text_file:
    nums_sum += int(num)
print(nums_sum)
text_file.close()
