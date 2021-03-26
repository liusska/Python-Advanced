[r, c] = [int(x) for x in input().split(", ")]

matrix = []
total = 0

for _ in range(r):
    row = [int(x) for x in input().split(", ")]
    total += sum(row)
    matrix.append(row)

print(total)
print(matrix)