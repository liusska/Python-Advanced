start = int(input())
end = int(input())

numbers = [x for x in range(start, end+1)]
numbers_to_ten = [x for x in range(2, 11)]

filtered_numbers = [num for num in numbers if any([num % x == 0 for x in numbers_to_ten])]

print(filtered_numbers)