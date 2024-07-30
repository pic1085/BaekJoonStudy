a, b, c = map(int,input().split())
num = divmod(a,b)
for i in range(c):
    num = divmod(num[1] * 10, b)
print(num[0])

# 경우의 수 N 이 100만 
# print(a // b) 몫
# print(a % b) 나머지
# for i in range(c):
    #A = num[1] * 10 % b
#print(A)