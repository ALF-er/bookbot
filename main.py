import sys
from stats import get_num_words, get_chars_counts, get_sorted_chars_counts

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_counts = get_chars_counts(book_text)
    sorted_chars_counts = get_sorted_chars_counts(chars_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in sorted_chars_counts:
        if char_count["char"].isalpha():
            print(f"{char_count["char"]}: {char_count["count"]}")
    print("============= END ===============")

main()
