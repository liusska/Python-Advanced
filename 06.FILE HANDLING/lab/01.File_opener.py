try:
    with open("text2.txt") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")