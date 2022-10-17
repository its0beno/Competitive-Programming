

stack = []
tokens = ["4", "13", "5", "/", "+"]
for i in tokens:
    if i not in ["+", "-", "*", "/"]:
        stack.append(int(i))
        print(stack)
    else:
        right = stack.pop()
        left = stack.pop()

        if i == '*':
            stack.append(right * left)

        elif i == '+':
            stack.append(left + right)

        elif i == '-':
            stack.append(left - right)

        elif i == '/':
            stack.append(int(left/right))
            print(stack)

print(stack.pop())
