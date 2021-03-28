def chair_combinations(names, size):
    def chairs_combinations_internal(names, size, combination, all_combinations):
        if len(combination) == size:
            all_combinations.append(combination[::])
            return
        for i in range(len(names)):
            name = names[i]
            combination.append(name)
            chairs_combinations_internal(names[i+1:], size, combination, all_combinations)
            combination.pop()
    all_combinations = []
    chairs_combinations_internal(names, size, [], all_combinations)
    return all_combinations


names = input().split(", ")
size = int(input())
result = chair_combinations(names, size)
[print(', '.join(x)) for x in result]