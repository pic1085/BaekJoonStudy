a = int(input())

for i in range(a):
    p, t = map(int, input().split())
    p = p + (t // 4) - (t // 7)
    print(p)
