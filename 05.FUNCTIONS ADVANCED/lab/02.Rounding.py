def round_num(numbers):
    return [round(x) for x in numbers]


nums = [float(x) for x in input().split()]
print(round_num(nums))