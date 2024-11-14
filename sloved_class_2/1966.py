import sys
from collections import deque
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    stack = deque(map(int, sys.stdin.readline().split()))
    
    if N == 1:
        print(1)
    else:
        time = 0
        for j in range(len(stack)):
            if stack[j] != M:
                time += 1
                stack.rotate(-1)
            elif stack[j] == M:
                print(time)
                
    