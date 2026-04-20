import datetime
name = input()
age = int(input())

print(f"{name}(은)는 {datetime.datetime.now().year-7+(100-age)}년에 100세가 될 것입니다.")

