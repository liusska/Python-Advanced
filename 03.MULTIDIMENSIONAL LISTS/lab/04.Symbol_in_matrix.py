n = int(input())

matrix = []
row_char = 0
col_char = 0

for _ in range(n):
    row = [str(x) for x in input()]
    matrix.append(row)

char = input()
is_equal = False

for row in range(len(matrix)):
    if char in matrix[row]:
        row_char = row
        col_char = matrix[row].index(char)
        is_equal = True
        break

if is_equal:
    print(f"({row_char}, {col_char})")
else:
    print(f"{char} does not occur in the matrix")

