def solution(ineq, eq, n, m):
    answer = 0
    if ineq == "<" and eq == "=":
        if n <= m:
            answer = 1
    elif ineq == "<" and eq == "!":
        if n < m:
            answer = 1
    elif ineq == ">" and eq == "=":
        if n >= m:
            answer = 1
    elif ineq == ">" and eq == "!":
        if n > m:
            answer = 1
    return answer

ineq = ">"
eq = "!"
n = 41
m = 78
print(solution(ineq, eq, n, m))