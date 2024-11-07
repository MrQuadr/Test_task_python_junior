def word_frequency(s: str) -> dict:
    signs = ",.!?;:"
    s_dict = {}
    
    for char in signs:
        s = s.replace(char, "")
    s = s.lower().split(" ")

    for i in s:
        if s_dict.get(i) is None:
            s_dict[i] = 1
        else:
            s_dict[i] += 1
    return s_dict

if __name__ == "__main__":
    text = "Hello, hello world! World. It's a beautiful world, isn't it?"
    print(word_frequency(text))
    pass