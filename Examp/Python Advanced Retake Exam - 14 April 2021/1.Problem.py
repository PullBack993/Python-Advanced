from collections import deque

def print_fail_orders(orders):
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in orders])}")
    exit()


pizza_orders = deque([int(el) for el in input().split(", ")])
employees = input().split(", ")
total_made_pizza = 0

while pizza_orders:
    first_order = pizza_orders.popleft()
    last_employee = employees.pop()

    if not last_employee.isdigit():
        print_fail_orders(pizza_orders)

    if first_order <= 0 or first_order > 10:
        employees.append(last_employee)

    elif first_order <= int(last_employee):
        total_made_pizza += first_order

    elif first_order > int(last_employee):
        total_made_pizza += int(last_employee)
        first_order -= int(last_employee)
        pizza_orders.appendleft(first_order)
        if not employees:
            print_fail_orders(pizza_orders)


if employees:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_made_pizza}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")

