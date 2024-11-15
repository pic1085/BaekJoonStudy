import sys
from collections import deque

for i in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    stack = deque(map(int, sys.stdin.readline().split()))
    li_dq = deque(range(0, N))
    time = 0
    
    while stack:
        if stack[0] == max(stack):
            time += 1
            stack.popleft()
            if li_dq.popleft() == M:
                print(time)
                break
        else:
            stack.rotate(-1)
            li_dq.rotate(-1)