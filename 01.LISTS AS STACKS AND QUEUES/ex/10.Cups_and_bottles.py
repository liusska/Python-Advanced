from collections import deque

cups_capacity = deque(int(x) for x in input().split(" "))
bottles_water = deque(int(x) for x in input().split(" "))

bottles = 0
wasted_litters = 0

while cups_capacity and bottles_water:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_water.pop()
    if current_bottle > current_cup:
        wasted_litters += current_bottle - current_cup
        current_bottle = current_bottle - current_cup
    elif current_cup > current_bottle:
        current_cup -= current_bottle
        cups_capacity.appendleft(current_cup)


if cups_capacity:
    print(f"Cups: {' '.join([str(x) for x in cups_capacity])}")
else:
    print(f"Bottles: {' '.join([str(x) for x in bottles_water])}")

print(f"Wasted litters of water: {wasted_litters}")