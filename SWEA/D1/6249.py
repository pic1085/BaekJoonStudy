num = int(input())
lst = [0]*10

while num > 0:
    lst[num%10] += 1
    num //= 10
    
print(' '.join(map(str, [num for num in range(10)])))
print(' '.join(map(str, lst)))

