from collections import deque

quantity = int(input())
names = input()
people = deque()
while names != 'Start':
    people.append(names)

    names = input()

command = input()
while command != "End":
    tokens = command.split(" ")
    if tokens[0] == "refill":
        quantity += int(tokens[1])
    else:
        if quantity >= int(tokens[0]):
            print(f"{people.popleft()} got water")
            quantity -= int(tokens[0])
        else:
            print(f"{people.popleft()} must wait")

    command = input()

print(f"{quantity} liters left")