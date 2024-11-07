def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]
    

if __name__ == "__main__":
    text = "A man a plan a canal Panama"
    print(is_palindrome(text))
    text = "A man a plan s canal Panama"
    print(is_palindrome(text))
    text = "A man a plan a Lanal Panama"
    print(is_palindrome(text))