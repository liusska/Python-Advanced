text = input()
vowels = "aouei"
no_vowels_text = ''.join([ch for ch in text if ch.lower() not in vowels])

print(no_vowels_text)