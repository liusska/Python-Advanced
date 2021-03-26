n = int(input())

longest_intersection_length = 0
longest_set = set()

for _ in range(n):
    command = input().split("-")
    [first_start, first_end] = command[0].split(",")
    [second_start, second_end] = command[1].split(",")
    first_set = set()
    second_set = set()
    for i in range(int(first_start), int(first_end)+1):
        first_set.add(i)
    for i in range(int(second_start), int(second_end)+1):
        second_set.add(i)
    current_intersection = first_set&second_set
    if len(current_intersection) > longest_intersection_length:
        longest_set = current_intersection
        longest_intersection_length = len(current_intersection)

print(f"Longest intersection is [{', '.join(str(x) for x in longest_set)}] with length {longest_intersection_length}")
