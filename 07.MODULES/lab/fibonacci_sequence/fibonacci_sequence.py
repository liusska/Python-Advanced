seq = [0, 1]


def create_sequence(n):
    global seq
    if n == 0:
        seq = []
    elif n == 1:
        seq = [0]
    else:
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
    print(f"{' '.join([str(x) for x in seq])}")


def locate(x):
    if x in seq:
        print(f"The number - {x} is at index {seq.index(x)}")
    else:
        print(f"The number {x} is not in the sequence")
