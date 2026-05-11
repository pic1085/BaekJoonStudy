def solution(n, control):
    answer = 0
    w = control.count("w")
    s = control.count("s")
    a = control.count("a")
    d = control.count("d")
    answer = n + w - s - (a * 10) + (d * 10)
    return answer

n = 0
control = "wsdawsdassw"
print(solution(n, control))
