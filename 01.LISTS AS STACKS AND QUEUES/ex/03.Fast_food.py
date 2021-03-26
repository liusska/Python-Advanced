from collections import deque

quantity_food = int(input())
orders = deque([int(x) for x in input().split(" ")])


print(max(orders))

while orders:
    if quantity_food > 0:
        current_order = orders.popleft()
        if quantity_food < current_order:
            orders.appendleft(current_order)
            print(f"Orders left: {' '.join([str(x) for x in orders])}")
            break
        else:
            quantity_food -= current_order

if not orders:
    print("Orders complete")