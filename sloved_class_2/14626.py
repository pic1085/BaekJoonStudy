isbm = input() # ISBN 코드 입력
result = 0 # 결과값 초기화
is_even = False # 짝수 자리수 여부

for i in range(13): # 13자리 반복
    if isbm[i] == '*': # '*' 발견 시
        if i % 2 != 0: # 홀수 자리수일 때
            is_even = True # 짝수 자리수 여부 True로 변경
        continue # 다음 반복으로 넘어감
    result += int(isbm[i]) * (1 if i %  2 == 0 else 3) # 가중치 곱하여 결과값에 더함
    
if is_even == True: # 짝수 자리수에 '*'가 있을 때
    for i in range(10): # 0~9까지 반복
        if (result + (i * 3)) % 10 == 0: # 결과값과 가중치 곱한 값이 10의 배수일 때
            print(i) # 출력
            break 
else:
    print(10 - result % 10) # 10에서 결과값을 10으로 나눈 나머지를 뺀 값을 출력