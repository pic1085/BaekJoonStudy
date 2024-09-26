import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    num_sum = sum((map(int, str(i))))
    hap = i + num_sum
    
    if hap == N:
        print(i)
        break
    if i == N:
        print(0)