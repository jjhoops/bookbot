def get_text(book_file):
    with open(book_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = dict()
    for ch in text:
        ch = ch.lower()
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count

def main():
    book_file = "books/frankenstein.txt"
    text = get_text(book_file)
    num_words = count_words(text)
    char_count = count_characters(text)
    print(f"--- Begin report of {book_file} ---")
    print(f"{num_words} words found in the document")
    print("")
    for key in char_count:
        if key.isalpha():
            print(f"The '{key}' charcter was found {char_count[key]} times")
    print("--- End report ---")

main()