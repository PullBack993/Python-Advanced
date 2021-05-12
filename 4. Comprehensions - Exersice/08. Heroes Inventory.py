# Input
# Peter, George
# Peter-Sword-20
# Peter-Shield-10
# George-Gem-100
# Peter-Sword-15
# George-Sword-20
# End

heroes = {hero: [] for hero in input().split(", ")}

command = input()
while not command == 'End':
    hero, item, price = command.split("-")
    if item not in heroes[hero]:
        heroes[hero] += [item, price]
    command = input()

for hero, items in heroes.items():
    price = [int(item) for item in items if item.isdecimal()]
    print(f"{hero} -> Items: {int(len(items))//2}, Cost: {sum(price)}")