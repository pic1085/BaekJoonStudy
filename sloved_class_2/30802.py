N = int(input())
count = 0
list_num = list(map(int, input(). split()))
P, T = map(int, input().split())

for i in range(0, 6):
    count += list_num[i] // P
    if list_num[i] % P > 0:
        count += 1    
print(count)
print(N // T, N % T)