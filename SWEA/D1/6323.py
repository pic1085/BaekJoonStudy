num = int(input())

def fibo(num):
    if num <= 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)
    
a = []

for i in range(1, num + 1):
    a.append(fibo(i))
    
print(a)