
def mul(a, b, c, d):
    if type(a and b and c and d) != int:
        return "에러발생"
    else:
        return a * b * c * d        
    
print(mul(1, 2, 3, '4'))