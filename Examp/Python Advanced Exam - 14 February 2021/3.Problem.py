def stock_availability(*args):
    inventory = args[0]
    data = args[1:]
    first_param = 'delivery'
    second_param = 'sell'
    if first_param in data:
        for el in data[1:]:
            inventory.append(el)
    elif second_param in data:
        if len(data) == 1:
            inventory.pop(0)
        elif str(data[1]).isnumeric():
            product_nums = int(data[1])
            for i in range(product_nums):
                inventory.pop(0)
        else:
            param = data[1:]
            set(inventory)
            for el in param:
                inventory = [i for i in inventory if i != el]


    return inventory

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


# ['choco', 'vanilla', 'banana', 'caramel', 'berry']
# ['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
# ['vanilla', 'banana']
# []
# ['banana']
# ['cookie', 'banana']
# ['chocolate', 'vanilla', 'banana']

