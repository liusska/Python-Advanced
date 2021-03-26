parentheses = input()

parentheses_as_stack = []
is_valid = True

for ch in parentheses:
    if ch == "{" or ch == "[" or ch == "(":
        parentheses_as_stack.append(ch)
    elif ch == "}" or ch == "]" or ch == ")":
        if not parentheses_as_stack:
            is_valid = False
            print("NO")
            break
        else:
            last_ch = parentheses_as_stack.pop()
            if last_ch == "{" and ch == "}":
                is_valid = True
            elif last_ch == "[" and ch == "]":
                is_valid = True
            elif last_ch == "(" and ch == ")":
                is_valid = True
            else:
                is_valid = False
                print("NO")
                break

if is_valid and not parentheses_as_stack:
    print("YES")




