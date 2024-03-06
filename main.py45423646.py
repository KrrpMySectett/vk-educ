import string
text = input()
words = text.split()
unique_words = set()
for word in words: 
    word = word.translate(str.maketrans(" ", " " , string.punctuation))
    word = word.lower()
    unique_words.add(word)
    for char in string.punctuation:
        word = word.replace(".", " ")
        word = word.replace(",", " ")
        word = word.replace("@", " ")
        word = word.replace("#", " ")
        word = word.replace("!", " ")
        word = word.replace("&", " ")
        word = word.replace("$", " ")
        word = word.replace(";", " ")
        word = word.replace(":", " ")
        word = word.replace("?", " ")
        word = word.replace("*", " ")
        word = word.replace("(", " ")
        word = word.replace(")", " ")
        word = word.replace("^", " ")
        word = word.replace("%", " ")
valid_words = []
for word in unique_words:
    if len(word) >= 5 and len(set(word)) >= 4 and words.count(word) > 2:
        valid_words.append(word) 
valid_words = sorted(valid_words)
valid_words = ' '.join(map(str,valid_words))
print(valid_words)