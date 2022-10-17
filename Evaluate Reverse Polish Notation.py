

stack = []
tokens = ["2", "1", "+", "3", "*"]
for i in tokens:
    if i not in ["+", "-", "*", "/"]:
        stack.append(int(i))
    else:
        right = stack.pop()
        left = stack.pop()

        if i == '*':
            stack.append(right * left)

        elif i == '+':
            stack.append(right + left)

        elif i == '-':
            stack.append(right - left)

        elif i == '/':
            stack.append(int(right / left))

print(stack.pop())
