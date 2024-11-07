def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
    

if __name__ == "__main__":
    text = "A man a plan a canal Panama"
    print(is_palindrome(text))
    text = "A man a plan s canal Panama"
    print(is_palindrome(text))
    text = "A man a plan a Lanal Panama"
    print(is_palindrome(text))