N = int(input())

if N == 1:
    print(1)
else:
    sum = 1
    i = 1
    while sum < N:
        sum += 6 * i
        i += 1
    print(i)