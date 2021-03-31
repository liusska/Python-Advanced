text = input()
repeat_count = input()

try:
    print(f"{text * int(repeat_count)}")
except ValueError:
    print("Variable times must be an integer")