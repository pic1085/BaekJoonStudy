def solution(a, b):
    answer = 0
    if str(a) + str(b) > str(b) + str(a):
        answer = int(str(a) + str(b))
    else:
        answer = int(str(b) + str(a))
    return answer

a = 8
b = 89
print(solution(a, b))