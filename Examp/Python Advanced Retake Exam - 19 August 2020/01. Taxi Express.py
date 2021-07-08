from collections import deque

customer = deque([int(el) for el in input().split(", ")])
taxi_num = [int(el) for el in input().split(", ")]
total_time = 0
while customer and taxi_num:
    first_customer = customer.popleft()
    last_taxi = taxi_num.pop()

    if last_taxi >= first_customer:
        total_time += first_customer
    elif first_customer > last_taxi:
        customer.appendleft(first_customer)

if customer:
    print(f"Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join([str(el) for el in customer])}")
else:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time} minutes")
