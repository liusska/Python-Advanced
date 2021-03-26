n = int(input())
name_set = set()

[name_set.add(input()) for _ in range(n)]

[print(name) for name in name_set]