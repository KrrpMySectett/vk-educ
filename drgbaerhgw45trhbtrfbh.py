def process_string(string):
    if string[0] == "!":
        processed_string = string.upper()
    else:
        processed_string = string.lower()
    processed_string = processed_string.replace("!", "").replace("@", "").replace("%", "")
    return processed_string
input_strings = ["Hello World!", "!Python programming language"]
for string in input_strings:
    processed_string = process_string(string)
    print(processed_string)