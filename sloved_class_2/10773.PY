sum = 0
stack = []
for i in range(int(input())):
    K = int(input())
    if K != 0:
        stack.append(K)
        sum += K
    else:
        sum -= stack.pop()
print(sum)