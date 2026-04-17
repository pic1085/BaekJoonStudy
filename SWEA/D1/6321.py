num = int(input())

def prime_num(num):
    if num < 2:
        return "소수가 아닙니다."
    for i in range(2, num):
        if num % i == 0:
            return "소수가 아닙니다."
    else:
        return "소수입니다."
    
print(prime_num(num))
