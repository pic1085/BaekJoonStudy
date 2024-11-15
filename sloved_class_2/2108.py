from collections import Counter
import sys

stack = []

for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    stack.append(a)

# 평균 계산
print(round(sum(stack) / len(stack)))

# 중앙값 계산
print(sorted(stack)[int((len(stack)+1)/2-1)])

# 최빈값 계산
counter = Counter(stack)
mode = counter.most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1]:  # 최빈값이 여러 개인 경우
    frequent_values = [item[0] for item in mode if item[1] == mode[0][1]]
    print(sorted(frequent_values)[1])  # 두 번째로 작은 값 출력
else:
    print(mode[0][0])

# 범위 계산
print(max(stack) - min(stack))
