def number_of_words(text):
    return len(text.split())


def count_characters(text):
    character_counts = {}
    for char in text.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts


def sort_on(item):
    return item["num"]


def sort_dictionary(character_counts):
    sorted_characters = []
    for char, num in character_counts.items():
        sorted_characters.append({"char": char, "num": num})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters