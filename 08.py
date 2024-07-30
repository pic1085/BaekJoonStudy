a = int(input())
B = 0
C = 0
for i in range(a):
    b = str(input())
    if b == 'D':
        B += 1
    if b == 'P':
        C += 1
    if B - C == 2 or C - B == 2:
        break
print("{}:{}".format(B,C))