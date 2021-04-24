numbers = int(input())
cars_parking = set()
for _ in range(numbers):
    command, car_numbers = input().split(", ")
    if command == 'IN':
        cars_parking.add(car_numbers)
    else:
        cars_parking.remove(car_numbers)

if cars_parking:
    for car in cars_parking:
        print(car)
else:
    print("Parking Lot is Empty")
