N = int(input())
list_num = list(map(int,input().split()))
count = 0

for i in range(N):
    if list_num[i] == 1:
        continue
    for j in range(2, list_num[i]):
        if list_num[i] % j == 0:
            break
    else:
        count += 1
print(count)