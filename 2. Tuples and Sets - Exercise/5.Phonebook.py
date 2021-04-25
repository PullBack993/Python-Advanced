phone_book = {}
while True:
    data = input()
    if data.isdigit():
        break
    people, phone = data.split("-")
    phone_book[people] = phone


for n in range(int(data)):
    name = input()
    if phone_book.get(name):
        print(f'{name} -> {phone_book[name]}')

    else:
        print(f'Contact {name} does not exist.')