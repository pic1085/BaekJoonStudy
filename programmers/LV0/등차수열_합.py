def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + (d * i)
    return answer

a = 7
d = 1
# included = [True, False, False, True, True]
included = [False, False, False, True, False, False, False]
print(solution(a, d, included))