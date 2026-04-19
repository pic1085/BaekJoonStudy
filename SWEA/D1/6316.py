lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_lst = list(filter(lambda x: x % 2 == 0, lst))

print(list(map(lambda x: x ** 2, new_lst)))