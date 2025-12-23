"""
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
"""

import sys
S = set() # 집합을 위해 선언

for i in range(int(sys.stdin.readline())):
    user = sys.stdin.readline().strip().split() # 유저의 입력을 받음 // 공백을 기준으로 분할
    
    if user[0] == "add": # add 명령어일 때
        S.add(int(user[1])) # 집합에 추가
    elif user[0] == "remove": # remove 명령어일 때
        S.discard(int(user[1])) # 집합에서 제거
    elif user[0] == "check": # check 명령어일 때
        print(1 if int(user[1]) in S else 0) # 집합에 있으면 1, 없으면 0 출력
    elif user[0] == "toggle": # toggle 명령어일 때
        if int(user[1]) in S: # 집합에 있으면
            S.remove(int(user[1])) # 제거
        else: # 집합에 없으면
            S.add(int(user[1])) # 추가
    elif user[0] == "all": # all 명령어일 때
        S = set(range(1, 21)) # 집합을 1부터 20까지의 숫자로 변경
    elif user[0] == "empty": # empty 명령어일 때
        S.clear() # 집합을 비움
        
        