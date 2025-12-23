'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
'''

N, K = map(int, input().split()) # 동전의 종류 수 N과 가치의 합 K 입력
coin = [] # 동전의 가치를 담을 리스트
temp = 0 # 동전의 개수를 담을 변수

for _ in range(N): 
    coin.append(int(input())) # 동전의 가치 입력
    coin.sort(reverse=True) # 동전의 가치를 내림차순으로 정렬

for i in range(N): 
    if coin[i] <= K: # 동전의 가치가 K보다 작거나 같을 때
        temp += K // coin[i] # 동전의 개수를 더함
        K = K % coin[i] # K를 동전의 가치로 나눈 나머지로 갱신
    else: 
        continue 
        
print(temp)
