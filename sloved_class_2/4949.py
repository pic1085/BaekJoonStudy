while True:
    N = input()
    stack =[]
    if N == '.':
        break
    
    for i in N:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        if i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")