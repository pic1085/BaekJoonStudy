N = int(input())
list_human = []

for i in range(N):
    a, b = map(int, input().split())
    list_human.append((a,b))
    
for j in list_human:
    rank = 1
    for k in list_human:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end=' ')