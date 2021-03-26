text = input()

st = []
for ch in text:
    st.append(ch)

reversed_text = []

while st:
    ch = st.pop()
    reversed_text.append(ch)

print(''.join(reversed_text))