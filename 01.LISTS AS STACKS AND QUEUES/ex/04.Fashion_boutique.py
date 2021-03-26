clothes = [int(x) for x in input().split(" ")]
capacity = int(input())
current_capacity = capacity
rack = 1

while clothes:
    current_clothes = clothes.pop()
    if current_capacity >= current_clothes:
        current_capacity -= current_clothes
    else:
        rack += 1
        current_capacity = capacity
        current_capacity -= current_clothes

print(rack)