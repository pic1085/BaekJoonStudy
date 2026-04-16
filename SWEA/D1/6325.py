lst = [2, 4, 6, 8, 10]

def find_num(num):
    if num in lst:
        return "True"
    else:
        return "False"

print(lst)
print(f"5 => {find_num(5)}")
print(f"10 => {find_num(10)}")