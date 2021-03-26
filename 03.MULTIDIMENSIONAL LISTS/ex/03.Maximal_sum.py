import sys
[row_count, col_count] = [int(x) for x in input().split()]

matrix = []
best_sum = -sys.maxsize
best_matrix = []
for _ in range(row_count):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for i in range(len(matrix) - 2):
    for j in range(col_count - 2):
        if matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2] > best_sum:
            best_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
            best_matrix = [[matrix[i][j], matrix[i][j+1], matrix[i][j+2]], [matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]], [matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]]


print(f"Sum = {best_sum}")
for row in best_matrix:
    print(" ".join([str(x) for x in row]))