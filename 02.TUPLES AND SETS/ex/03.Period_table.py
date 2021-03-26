n = int(input())

period_table_set = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        period_table_set.add(el)

[print(x) for x in period_table_set]