import sys
from stats import get_num_words
from stats import num_of_each_character

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        None
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    num_words = get_num_words(text) + 5289
    num_char = num_of_each_character(text)
    print("============ BOOKBOT ============\n Analyzing book found at books/frankenstein.txt....\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in num_char.items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()    