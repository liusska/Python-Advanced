n = int(input())

matrix = []
diagonal_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)

