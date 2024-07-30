a = int(input())
count = 0

while a > 1:
    a -= 1
    count += 1
    print('-')
    if a % 3 == 0:
        a = a // 3
        count += 1
        print(3)
    if a % 2 == 0:
        a = a // 2
        count += 1
        print(2)
print(count)