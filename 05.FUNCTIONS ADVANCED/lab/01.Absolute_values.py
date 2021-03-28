def abs_val(numbers):
    return [abs(x) for x in numbers]


nums = [float(x) for x in input().split(" ")]
print(abs_val(nums))