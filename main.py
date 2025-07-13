from stats import get_num_words, count_characters, sorted_chars
import sys

def get_text(book_file):
    with open(book_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    text = get_text(book_file)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    '''
    print(f"--- Begin report of {book_file} ---")
    print(f"{num_words} words found in the document")
    print("")
    print(sorted_chars(char_count))
    '''
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for entry in sorted_chars(char_count):
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")            

main()