from lab.fibonacci_sequence.fibonacci_sequence import *

fibonacci_sequence_commands = []
while True:
    command = input()
    if command == "Stop":
        break
    else:
        fibonacci_sequence_commands.append(command)


for command in fibonacci_sequence_commands:
    if 'Create' in command:
        number = int(command.split()[2])
        create_sequence(number)
    else:
        number = int(command.split()[1])
        locate(number)
