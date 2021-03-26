line = [float(x) for x in input().split(" ")]
values = {}
for l in line:
    if l not in values:
        values[l] = 0
    values[l] += 1

for (key, value) in values.items():
    print(f"{key} - {value} times")