import sys

def re_round(value):
    if value - int(value) >= 0.5:
        return int(value) + 1
    else:
        return int(value)
    
N = int(sys.stdin.readline())
if N == 0: print(0)
else:
    val = re_round(N*0.15)
    li = []
    
    for i in range(N):
        num = int(sys.stdin.readline())
        li.append(num)
        
    li.sort()
    print(re_round(sum(li[val:N-val]) / len(li[val:N-val])))