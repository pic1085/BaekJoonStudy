N = int(input())
list_char = list(map(str, input()))
count = 0

for i in range(N):
    count += (ord(list_char[i]) - 96) * (31**i)
    
print(count % 1234567891)