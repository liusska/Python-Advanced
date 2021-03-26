[n, m] = input().split(" ")

n_set = set()
m_set = set()

[n_set.add(input()) for _ in range(int(n))]
[m_set.add(input()) for _ in range(int(m))]

new_set = n_set.intersection(m_set)

[print(x) for x in new_set]