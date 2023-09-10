message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:
    if 'a' <= ch <= 'z':
        pos = (ord(ch) - ord('a') + offset) % 26
        new_char = chr(pos + ord('a'))
    elif 'A' <= ch <= 'Z':
        pos = (ord(ch) - ord('A') + offset) % 26
        new_char = chr(pos + ord('A'))
    else:
        new_char = ch

    encoded_message += new_char

print("Encoded message:", encoded_message)