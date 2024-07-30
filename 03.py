# 14912 문제
a, b = map(int, input().split())
temp = ''
for i in range(1,a+1):
    temp+=str( i )
print(temp.count(str(b)))