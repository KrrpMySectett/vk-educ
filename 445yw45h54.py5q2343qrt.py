def remove_punctuation(input_string):
    punctuation_chars = "!.,?;:#$%^&*()"
    clean_string = ""
    for char in input_string:
        if char not in punctuation_chars:
            clean_string += char
    return clean_string


def process_string(input_string):
    input_string = remove_punctuation(input_string.lower())

    words = input_string.split()

    word_count = {}
    for word in words:
        if len(word) >= 5 and len(set(word)) >= 4:
            word_count[word] = word_count.get(word, 0) + 1

    filtered_words = [word for word, count in word_count.items() if count > 2]

    filtered_words.sort()
    return filtered_words


text = input().replace("\\", " ")
result = process_string(text)
for i in result:
    print(i)