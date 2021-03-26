n = int(input())
matrix = []
primary_diagonal = 0
secondary_diagonal = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for i in range(len(matrix)):
    primary_diagonal += matrix[i][i]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i + j == n - 1:
            secondary_diagonal += matrix[i][j]

diff = abs(primary_diagonal - secondary_diagonal)
print(diff)