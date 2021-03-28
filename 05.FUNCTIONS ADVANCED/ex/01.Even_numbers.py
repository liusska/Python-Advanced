def is_even(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


numbers = [int(x) for x in input().split()]
print(is_even(numbers))