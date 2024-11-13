from collections import deque

N, K = map(int, input().split())
stack = deque(range(1, N + 1))
result = []
for i in range(N):
    stack.rotate(-K)
    result.append(stack.pop())
    
print("<", end= "")
for j in range(N-1):
    print(result[j], end= ", ")
print(result[N-1], end= "")
print(">")

