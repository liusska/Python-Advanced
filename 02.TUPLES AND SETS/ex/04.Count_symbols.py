text = input()

symbol_dict = {}

for ch in text:
    if ch not in symbol_dict:
        symbol_dict[ch] = 0
    symbol_dict[ch] += 1

sorted_dict = dict(sorted(symbol_dict.items(), key=lambda x:x[0]))

for (key, value) in sorted_dict.items():
    print(f"{key}: {value} time/s")