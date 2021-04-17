from collections import deque
quantity = int(input())
orders_input = list(map(int, input().split()))
orders = deque(orders_input)

print(max(orders_input))
for order in orders_input:
    if quantity >= order:
        quantity -= order
        orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")