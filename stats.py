def number_of_words(text):
    return f"Found {len(text.split())} total words"

def count_characters(text):
    text = text.lower()
    textdic = {}
    for char in text:
        if char in textdic:
            textdic[char] += 1
        else:
            textdic[char] = 1
    return textdic