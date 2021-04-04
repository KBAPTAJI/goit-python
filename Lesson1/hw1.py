message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        if 97 <= (ord(ch) + offset) <= 122:
            while offset > 26:
                offset -= 26
            encoded_message += chr(ord(ch) + offset)
        elif 122 < (ord(ch) + offset) < 150:
            while offset > 26:
                offset -= 26
            i = ord(ch) - 122 + 96 + offset
            encoded_message += chr(i)
        elif 65 <= (ord(ch) + offset) <= 90:
            while offset > 26:
                offset -= 26
            encoded_message += chr(ord(ch) + offset)
        else:
            while offset > 26:
                offset -= 26
            i = ord(ch) - 90 + 64 + offset
            encoded_message += chr(i)
    else:
        encoded_message += ch
print(f'Закодированное слово: {encoded_message}')
