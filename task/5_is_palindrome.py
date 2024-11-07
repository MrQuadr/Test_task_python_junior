def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    
    for i, j in enumerate(s[:(len(s)//2+1)], start=1):
        if j != s[-i]:
            return False
    return True
    

if __name__ == "__main__":
    text = "A man a plan a canal Panama"
    print(is_palindrome(text))
    text = "A man a plan s canal Panama"
    print(is_palindrome(text))
    text = "A man a plan a Lanal Panama"
    print(is_palindrome(text))