from collections import deque


def solve():
    people = deque()
    command = input()
    while command != "End":
        if command == "Paid":
            while people:
                print(people.popleft())
        else:
            people.append(command)
        command = input()
    print(f"{len(people)} people remaining.")


solve()