def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts

def sort_character_count(char_counts):
    sorted_list = [{"char": char, "count": count} for char, count in char_counts.items()]
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list