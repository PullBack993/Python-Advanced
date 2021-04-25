num = int(input())
intersections = []
for n in range(num):
    first_pair, second_pair = input().split("-")
    f_start, f_stop = [int(el) for el in first_pair.split(',')]
    s_start, s_stop = [int(el) for el in second_pair.split(',')]
    first = range(f_start, f_stop+1)
    second = range(s_start, s_stop+1)
    intersection = set(first).intersection(second)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]

print(f'Longest intersection is {[*longest]} with length {len(longest)}')