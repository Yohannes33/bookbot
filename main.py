from stats import number_of_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    #print(text)
    print(number_of_words(text))

    count_character = count_characters(text)
    print(count_character)

main()

