# 17356 문제
a, b = map(int, input().split())

m = (b - a) / 400
win = 1 / (1 + 10 ** m)

print(win)