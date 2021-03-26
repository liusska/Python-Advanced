[row_count, col_count] = [int(x) for x in input().split()]

matrix = []
equal_squares = 0

for _ in range(row_count):
    row = [str(x) for x in input().split()]
    matrix.append(row)

for i in range(len(matrix) - 1):
    for j in range(col_count - 1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            equal_squares += 1

print(equal_squares)