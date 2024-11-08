hap = 0
for i in range(int(input())):
    for j in input().split('X'): 
        hap += sum(range(1, len(j)+1)) 
    print(hap)
    hap = 0