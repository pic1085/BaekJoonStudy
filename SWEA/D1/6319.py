def Palindrome(word):
    if word == word[::-1]:
        return word[::-1], "입력하신 단어는 회문(Palindrome)입니다."
    else:
        return word[::-1], "입력하신 단어는 회문(Palindrome)이 아닙니다."
    
word = input()
print(Palindrome(word)[0])
print(Palindrome(word)[1])