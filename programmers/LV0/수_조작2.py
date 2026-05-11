def solution(numLog):
    answer = ''
    w = 1
    s = -1
    d = 10
    a = -10
    for i in range(len(numLog)):
        if i == 0:
            continue
        elif numLog[i] - numLog[i-1] == w:
            answer += 'w'
        elif numLog[i] - numLog[i-1] == s:
            answer += 's'
        elif numLog[i] - numLog[i-1] == d:
            answer += 'd'
        elif numLog[i] - numLog[i-1] == a:
            answer += 'a'
    return answer
    
numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(numLog))
