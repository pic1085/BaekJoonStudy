a = int(input())
for i in range(a):
    H, W, N = map(int, input().split())
    count = N // H + 1
    floor = N % H
    if N % H == 0:
        count = N // H
        floor = H
    print(floor * 100 + count)