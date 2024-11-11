for i in range(int(input())):
    N = input()
    stack = []
    for w in N:
        if w == '(':
            stack.append(w)
        elif w == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(w)
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")