def solution(num_list):
    answer = 0
    n = []
    m = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            n.append(num_list[i])
        else:
            m.append(num_list[i])
    return int(''.join(map(str, n))) + int(''.join(map(str, m)))

num_list = [5, 7, 8, 3]
print(solution(num_list))