import sys

input = sys.stdin.readline # 빠른 입력을 위해 sys 모듈 사용
n = int(input()) # 목표 숫자 입력
d = [0] * (n + 1) # 0부터 n까지의 리스트 생성

for i in range(2, n + 1): # 2부터 n까지 반복
    d[i] = d[i - 1] + 1 
    if i % 3 == 0: # 3으로 나누어 떨어질 때
        d[i] = min(d[i], d[i // 3] + 1) # 3으로 나누는 경우와 비교하여 최소값 저장
    if i % 2 == 0: # 2로 나누어 떨어질 때
        d[i] = min(d[i], d[i // 2] + 1) # 2로 나누는 경우와 비교하여 최소값 저장

print(d[n])