usernames = set()
n = int(input())

[usernames.add(input()) for _ in range(n)]

[print(name) for name in usernames]