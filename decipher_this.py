decipher_message = input().split()

for message in decipher_message:
    char_codes = [digit_or_char for digit_or_char in message if digit_or_char.isdigit()]
    char_code = "".join(char_codes)
    text = [digit_or_char for digit_or_char in message if digit_or_char.isalpha()]

    text[0], text[-1] = text[-1], text[0]
    text.insert(0, chr(int(char_code)))

    print("".join(text), end= " ")