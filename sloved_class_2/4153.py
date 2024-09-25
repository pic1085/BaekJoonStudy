while True:
    list_num= list(map(int, input().split()))
    list_num.sort()
    
    if sum(list_num) == 0:
        break
    if list_num[0]*list_num[0] + list_num[1]*list_num[1] == list_num[2]*list_num[2]:
        print("right")
    else:
        print("wrong")
