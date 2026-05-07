def solution(number, n, m):
    answer = 0
    if number % n == 0 and number % m == 0:
        answer = 1
    else:
        answer = 0
    return answer

number = 55
n = 10
m = 5
print(solution(number, n, m))