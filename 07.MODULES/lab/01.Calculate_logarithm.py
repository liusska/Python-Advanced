from math import log


def calc_log(num, base):
    if base == "natural":
        return log(num)
    else:
        return log(num, int(base))


log_number = calc_log(int(input()), input())
print(f"{log_number:.2f}")