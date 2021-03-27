words = input().split(", ")

words_with_length = [f"{word} -> {len(word)}" for word in words]
print(", ".join(words_with_length))