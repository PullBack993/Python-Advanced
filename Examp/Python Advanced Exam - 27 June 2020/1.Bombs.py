from collections import deque

COMBINATION = {"datura": 40,
               "cherry": 60,
               "smoke": 120, }


def check_combination(total):
    for key, value in COMBINATION.items():
        if value == total:
            return key


bomb_effect = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]
datura = 0
cherry = 0
smoke = 0

while not datura >= 3 or not cherry >= 3 or not smoke >= 3:
    if bomb_effect and bomb_casings:
        comb = check_combination(bomb_effect[0] + bomb_casings[-1])
        if comb:
            bomb_effect.popleft()
            bomb_casings.pop()
            if 'datura' == comb:
                datura += 1
            elif 'cherry' == comb:
                cherry += 1
            else:
                smoke += 1
        else:
            bomb_casings[-1] -= 5
    else:
        break

if datura >= 3 and cherry >= 3 and smoke >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join([str(e) for e in bomb_effect])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(c) for c in bomb_casings])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry}")
print(f"Datura Bombs: {datura}")
print(f"Smoke Decoy Bombs: {smoke}")
