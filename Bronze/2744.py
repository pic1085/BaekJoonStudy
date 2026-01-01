n = input()

for i in range(len(n)):
    if ord(n[i]) >= 97:
        print(chr(ord(n[i]) - 32), end = '')
    else:
        print(chr(ord(n[i]) + 32), end = '')
