count = 1 # 현재 수
status = True # 가능 여부
stack = [] # 스택
sign= [] # 부호 기록용

for i in range(int(input())): # 반복
    num = int(input()) # 수 입력
    
    while count <= num: # 현재 수가 입력 수보다 작거나 같을 때
        stack.append(count) # 스택에 현재 수 추가
        sign.append("+") # 부호 기록
        count += 1 # 현재 수 증가
        
    if stack[-1] == num: # 스택의 최상단 수가 입력 수와 같다면
        stack.pop() # 스택에서 최상단 수 제거
        sign.append("-") # 부호 기록
        
    else: # 스택의 최상단 수가 입력 수와 다르다면
        status = False # 불가능
        break # 반복문 탈출

if status == False: # 불가능하다면
    print("NO") # NO 출력
else: # 가능하다면
    for i in sign: # 부호 기록 순서대로
        print(i) # 출력
