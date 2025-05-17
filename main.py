import sys
from stats import (
    get_num_words, 
    get_char_count, 
    sort_chars, 
    print_chars )

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")    
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    text_file = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    num_words = get_num_words(text_file)
    print(f"Found {num_words} total words")
        
    print("--------- Character Count -------")
    print_chars(sort_chars(get_char_count(text_file)))
    
    print("============= END ===============")
    return 0

main()
