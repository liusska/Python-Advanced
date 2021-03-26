[row_count, col_count] = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(row_count):
    row = [int(x) for x in input().split()]
    matrix.append(row)

column_sum = [0] * col_count

for row in range(row_count):
    for col in range(col_count):
        column_sum[col] += matrix[row][col]

[print(x) for x in column_sum]