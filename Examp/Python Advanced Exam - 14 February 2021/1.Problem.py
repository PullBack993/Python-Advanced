from collections import deque


def check_positive(num):
    if num <= 0:
        return True
    return False


firework_effect = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]
palm = 0
willow = 0
crossette = 0
while not palm >= 3 or not willow >= 3 or not crossette >= 3:
    if firework_effect and explosive_power:

        first_firework = firework_effect.popleft()
        if check_positive(first_firework):
            continue
        last_explosive = explosive_power.pop()
        if check_positive(last_explosive):
            if not check_positive(first_firework):
                firework_effect.appendleft(first_firework)
                continue
            else:
                continue

        sum_values = first_firework + last_explosive
        if sum_values % 3 == 0 and sum_values % 5 != 0:
            palm += 1
        elif sum_values % 5 == 0 and sum_values % 3 != 0:
            willow += 1
        elif sum_values % 3 == 0 and sum_values % 5 == 0:
            crossette += 1
        else:
            explosive_power.append(last_explosive)
            firework_effect.append(first_firework - 1)
    else:
        break

if palm >= 3 and willow >= 3 and crossette >= 3:
    print("Congrats! You made the perfect firework show!")
    if firework_effect:
        print(f"Firework Effects left: {', '.join([str(el) for el in firework_effect])}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
    print(f"Palm Fireworks: {palm}")
    print(f"Willow Fireworks: {willow}")
    print(f"Crossette Fireworks: {crossette}")

else:
    print("Sorry. You can't make the perfect firework show.")
    if firework_effect:
        print(f'Firework Effects left: {", ".join([str(el) for el in firework_effect])}')
    if explosive_power:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
    print(f"Palm Fireworks: {palm}")
    print(f"Willow Fireworks: {willow}")
    print(f"Crossette Fireworks: {crossette}")
