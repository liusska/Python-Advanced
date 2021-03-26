n = int(input())
parking_set = set()

for _ in range(n):
    [action, car_number] = input().split(", ")
    if action == "IN":
        parking_set.add(car_number)
    elif action == "OUT":
        parking_set.remove(car_number)

if parking_set:
    [print(car) for car in parking_set]
else:
    print("Parking Lot is Empty")