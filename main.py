import sys
from stats import get_word_count, get_count_of_characters, character_report

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filename = sys.argv[1]
    book_text = get_book_text(filename)
    num_words = get_word_count(book_text)
    num_characters = get_count_of_characters(book_text)
    book_report = character_report(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}")
    print("----------- Word Count ----------")
    print(f" Found {num_words} total words")
    print("--------- Character Count -------")
    for char in book_report:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()