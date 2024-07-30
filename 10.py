a = int(input())
for i in range(a):
    candy = []
    m = 0
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    for j in candy:
        m += j // k
    print(m)