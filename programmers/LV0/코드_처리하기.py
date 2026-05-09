def solution(code):
    answer = ''
    mod = 0
    for i in range(0, len(code)):
        if code[i] == "1":
            mod += 1
        else:   
            if mod % 2 == 0:
                if i % 2 == 0:
                    answer += code[i]
            else:
                if i % 2 != 0:
                    answer += code[i]
    if answer == "":
        answer = "EMPTY"
    return answer
    
code = "abc1abc1abc"
print(solution(code))