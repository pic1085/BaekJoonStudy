lst = []
for i in range(4):
    lst.append(input())

def game(lst):
    if "가위" and "바위" in lst:
        return "바위가 이겼습니다!"
    elif "가위" and "보" in lst:
        return "가위가 이겼습니다!"
    elif "바위" and "보" in lst:
        return "보가 이겼습니다!"
    
print(game(lst))