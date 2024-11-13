from collections import deque

N = deque(range(1,int(input())+1))
for i in range(len(N)-1):
    N.popleft()
    N.rotate(-1)
print(N[0])
