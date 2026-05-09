def solution(num_list):
    answer = 0
    s = sum(num_list)
    p = 1
    for i in num_list:
        p *= i
    if s ** 2 > p:
        answer = 1
    else:
        answer = 0
    return answer
num_list = [5, 7, 8, 3]
print(solution(num_list))
