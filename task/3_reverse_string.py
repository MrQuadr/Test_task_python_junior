def reverse_string(s: str) -> str:
    return s[::-1]
    

if __name__ == "__main__":
    text = "Hello, hello world! World. It's a beautiful world, isn't it?"
    print(reverse_string(text))