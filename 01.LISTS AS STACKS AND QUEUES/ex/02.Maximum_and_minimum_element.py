from _collections import deque

n = int(input())
stack = deque()

for _ in range(n):
    command = input().split()
    if command[0] == "1":
        stack.appendleft(int(command[1]))
    elif command[0] == "2":
        if stack:
            stack.popleft()
    elif command[0] == "3":
        if stack:
            print(f"{max(stack)}")
    elif command[0] == "4":
        if stack:
            print(f"{min(stack)}")

print(", ".join([str(x) for x in stack]))
