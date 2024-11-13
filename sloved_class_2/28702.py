for i in range(3,0,-1):
    x = input()
    if x not in ["Fizz", "Buzz", "FizzBuzz"]:
        num = int(x) + i
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num %3 == 0 and num % 5 != 0:
    print("Fizz")
elif num % 3 != 0 and num % 5 == 0:
    print("Buzz")
else:
    print(num)
    