def comparison(a, b):
    if len(a) > len(b):
        return a
    else:
        return b
    
a, b = map(str, input().split(', '))
print(comparison(a, b))