lst = [12,24,35,24,88,120,155,88,120,155]

def delete_num(lst):
    a = set(lst)
    return list(sorted(a))

print(delete_num(lst))