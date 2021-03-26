numbers = [str(x) for x in input().split(' ')]

while numbers:
    print(f'{numbers.pop()}', end=" ")