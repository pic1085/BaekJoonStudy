def square(a, b):
    return a ** 2, b ** 2

a, b = map(int, input().split(', '))

print(f"square({a}) => {square(a, b)[0]}")
print(f"square({b}) => {square(a, b)[1]}")