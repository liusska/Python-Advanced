[row_count, col_count] = [int(x) for x in input().split()]

matrix = []

for _ in range(row_count):
    row = input().split()
    matrix.append(row)

command = input()
while command != "END":
    tokens = command.split()
    if "swap" in tokens and len(tokens) == 5:
        row1 = int(tokens[1])
        col1 = int(tokens[2])
        row2 = int(tokens[3])
        col2 = int(tokens[4])
        if row1 < row_count and row2 < row_count and col1 < col_count and col2 < col_count:
            current_row = matrix[row1][col1]
            matrix[row1][col1] = matrix[row2][col2]
            matrix[row2][col2] = current_row
            for row in matrix:
                print(' '.join(row))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()
