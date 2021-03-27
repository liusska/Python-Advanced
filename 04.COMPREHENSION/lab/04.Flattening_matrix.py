rows = int(input())
numbers_list = []
for row in range(rows):
    numbers_list += [int(x) for x in input().split(", ")]

print(numbers_list)
