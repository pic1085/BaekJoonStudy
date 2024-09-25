import sys
arr = []
for j in range(32):
    arr.append(2**j)
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a in arr:
        print(1)
    else:
        print(0)