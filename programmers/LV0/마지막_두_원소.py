def solution(num_list):
    answer = []
    for i in range(len(num_list)):
        answer.append(num_list[i])
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)
    return answer

num_list = [5, 2, 1, 7, 5]
print(solution(num_list))