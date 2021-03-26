command = input()
phonebook = {}
while not command.isdigit():
    [name, number] = command.split("-")
    if name not in phonebook:
        phonebook[name] = ""
    phonebook[name] = number
    command = input()

n = int(command)

for _ in range(n):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
