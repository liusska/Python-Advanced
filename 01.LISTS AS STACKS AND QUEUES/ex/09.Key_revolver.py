from collections import deque

price_for_bullet = int(input())
size_gun_barrel = int(input())
bullets = deque([int(x) for x in input().split(" ")])
locks = deque([int(x) for x in input().split(" ")])
intelligence = int(input())

count_shouts = 0
current_size_gun_barrel = size_gun_barrel
while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    current_size_gun_barrel -= 1
    count_shouts += 1
    if current_size_gun_barrel == 0 and bullets:
        current_size_gun_barrel = size_gun_barrel
        print("Reloading!")
    if not bullets and locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
    elif not locks:
        price = count_shouts * price_for_bullet
        print(f"{len(bullets)} bullets left. Earned ${intelligence - price}")

