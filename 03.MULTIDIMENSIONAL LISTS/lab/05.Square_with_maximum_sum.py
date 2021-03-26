import sys
[row_count, col_count] = [int(x) for x in input().split(", ")]

matrix = []
max_matrix = []
max_square = -sys.maxsize

for _ in range(row_count):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

for row in range(row_count - 1):
    for col in range(col_count - 1):
        if matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1] > max_square:
            max_square = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
            max_matrix = [[matrix[row][col], matrix[row][col+1]], [matrix[row+1][col], matrix[row+1][col+1]]]

for row in range(len(max_matrix)):
    print(" ".join(str(x) for x in max_matrix[row]))
print(max_square)


