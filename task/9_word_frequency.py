import re

def word_frequency(s: str) -> dict:
    s = re.sub(r'[^a-zA-Z\s]', '', s).lower().split()
    
    s_dict = {}
    for i in s:
        s_dict[i] = s_dict.get(i, 0) + 1
    return s_dict

if __name__ == "__main__":
    text = "Hello, hello world! World. It's a beautiful world, isn't it?"
    print(word_frequency(text))