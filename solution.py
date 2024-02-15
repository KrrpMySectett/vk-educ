line = input()
words = []
current_word = ""
for char in line:
    if char.isalnum():
        current_word += char
    elif current_word:
        words.append(current_word)
        current_word = ""
if current_word:
    words.append(current_word)
word_counts = {}
for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1 
most_common_word = ""
most_common_count = 0
for word, count in word_counts.items():
    if count > most_common_count:
        most_common_word = word
        most_common_count = count
print(most_common_word, most_common_count)