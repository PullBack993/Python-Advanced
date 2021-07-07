from collections import deque


def check_value(m, f):
    if m <= 0 or f <= 0:
        return False
    return True


def check_spc_case_f(value):
    if value % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    return True


def check_spc_case_m(value):
    if value % 25 == 0:
        males.pop()
        if males:
            males.pop()
    return True


def equal(first_f, last_m):
    if first_f == last_m:
        females.popleft()
        males.pop()
        return True
    else:
        females.popleft()
    males[-1] -= 2
    return False


males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])
matches = 0
while males and females:

    first_females = females[0]
    last_males = males[-1]

    if check_value(first_females, last_males):

        if check_spc_case_f(first_females):
            continue

        if check_spc_case_m(last_males):
            continue

        if equal(first_females, last_males):
            matches += 1

    else:
        if last_males <= 0:
            males.pop()
        else:
            females.popleft()

print(f"Matches: {matches}")
if males:
    prep_print = ", ".join([str(el) for el in reversed(males) if el > 0])
    print(f"Males left: {prep_print}")
else:
    print("Males left: none")
if females:
    prep_print = ", ".join([str(el) for el in females if el > 0])
    print(f"Females left: {prep_print}")
else:
    print("Females left: none")
