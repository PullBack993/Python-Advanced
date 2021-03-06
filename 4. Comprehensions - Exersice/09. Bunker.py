categories = {category: [] for category in input().split(", ")}

quantity = 0
quality = 0

for _ in range(int(input())):
    data = input().split(" - ")
    categories[data[0]].append(data[1])

    information_data = data[2].split(";")
    quantity += int(information_data[0].split(":")[1])
    quality += int(information_data[1].split(":")[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {quality / len(categories):.2f}")
[print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]

# input
# food, water, materials, metal
# 5
# food - pizza - quantity:10;quality:5
# water - mineral - quantity:5;quality:10
# materials - wood - quantity:2;quality:5
# metal - copper - quantity:3;quality:10
# food - burgers - quantity:5;quality:2
