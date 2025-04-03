def get_num_words(text):
    return len(text.split())

def get_chars_counts(text):
    chars_counts = {}

    for char in text:
        char_lower = char.lower()
        chars_counts[char_lower] = chars_counts.get(char_lower, 0) + 1

    return chars_counts

def get_sorted_chars_counts(chars_counts):
    result = [{"char": k, "count": v} for k, v in chars_counts.items()]
    result.sort(reverse=True, key=lambda dict: dict["count"])
    return result
