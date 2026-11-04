def is_palindrom(s):
    if s == s[::-1]:
        return "palindrome"
    else:
        return"not pallindrom"
print(is_palindrom("madam"))
print(is_palindrom("python"))    