def expressions(numbers, current_result=0, expression=''):
    if not numbers:
        return [(expression, current_result)]
    result_plus = expressions(
        numbers[1:],
        current_result + numbers[0],
        f'{expression}+{numbers[0]}')
    result_minus = expressions(
        numbers[1:],
        current_result - numbers[0],
        f'{expression}-{numbers[0]}')
    return result_plus + result_minus


result = [int(x) for x in input().split(", ")]
print(*[f'{x[0]}={x[1]}' for x in expressions(result)], sep="\n")