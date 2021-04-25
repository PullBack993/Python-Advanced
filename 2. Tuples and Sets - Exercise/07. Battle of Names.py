def modified_set_equal(even_num_set, odd_num_set):
    modified_set = [str(el) for el in even_num_set.union(odd_num_set)]
    return modified_set


def modified_set_diferentce(even_num_set, odd_num_set):
    modified_set = [str(el) for el in odd_num_set.difference(even_num_set)]
    return modified_set

def modified_set_sym(even_num_set, odd_num_set):
    modified_set = [str(el) for el in even_num_set.symmetric_difference(odd_num_set)]
    return modified_set


number = int(input())
even_num = set()
odd_num = set()
ascii_value = []

for n in range(1, number+1):
    data = input()
    current_sum = sum([ord(el) for el in data]) // n
    if current_sum % 2 == 0:
        even_num.add(current_sum)
    else:
        odd_num.add(current_sum)

sum_evens = sum(even_num)
sum_odds = sum(odd_num)

if sum_evens == sum_odds:
    print(f"{', '.join(modified_set_equal(even_num,odd_num))}")
elif sum_odds > sum_evens:
    print(f"{', '.join(modified_set_diferentce(even_num,odd_num))}")
else:
    print(f"{', '.join(modified_set_sym(even_num,odd_num))}")
