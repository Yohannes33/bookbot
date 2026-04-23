def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def number_of_words(text):
    return f"Found {len(text.split())} total words"

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    print(number_of_words(text))

main()

