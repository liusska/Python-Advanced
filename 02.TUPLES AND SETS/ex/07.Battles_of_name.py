n = int(input())
odd_sum_names = set()
even_sum_names = set()

for line in range(1, n + 1):
    current_sum = 0
    name = input()
    for ch in name:
        current_sum += ord(ch)
    current_sum //= line
    if current_sum % 2 == 0:
        even_sum_names.add(current_sum)
    else:
        odd_sum_names.add(current_sum)

if sum(odd_sum_names) == sum(even_sum_names):
    union_set = odd_sum_names.union(even_sum_names)
    print(f"{', '.join(str(x) for x in union_set)}")
elif sum(odd_sum_names) > sum(even_sum_names):
    difference_set = odd_sum_names.difference(even_sum_names)
    print(f"{', '.join(str(x) for x in difference_set)}")
elif sum(even_sum_names) > sum(odd_sum_names):
    symmetric_difference_set = odd_sum_names.symmetric_difference(even_sum_names)
    print(f"{', '.join(str(x) for x in symmetric_difference_set)}")