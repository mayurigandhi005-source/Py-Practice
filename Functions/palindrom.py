def is_palindrome(text: str) -> bool:
    
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned == cleaned[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("Hello, World!"))                   # Output: False