def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    characters = {}

    for c in text:
        std_char = c.lower()
        if std_char not in characters:
            characters[std_char] = 1
        else:
            characters[std_char] += 1
    return characters

def print_chars(chars):
    for key, value in chars.items():
        print(f"{key}: {value}")
    return 0

def sort_chars(chars):
    return dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
