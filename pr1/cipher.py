ru = [chr(i) for i in range(ord('а'), ord('я') + 1)]
en = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def text_caesar(alphabet, text, shift):
    alphabet_lower = "".join(alphabet)
    alphabet_upper = "".join(alphabet_lower.upper())

    ord_first_letter_lower = ord(alphabet_lower[0])
    ord_first_letter_upper = ord(alphabet_upper[0])

    new_text = ""

    for symbol in text:
        if symbol in alphabet_lower:
            new_text += chr((ord(symbol) - ord_first_letter_lower + shift) % len(alphabet) + ord_first_letter_lower)
        elif symbol in alphabet_upper:
            new_text += chr((ord(symbol) - ord_first_letter_upper + shift) % len(alphabet) + ord_first_letter_upper)
        else:
            new_text += symbol

    return new_text

def decrypt_text_caesar(alphabet, text, shift):
    return text_caesar(alphabet, text, -shift)

direction = input("Действие (шифрование - 1, дешифрование - 2): ")
user_lang = input("Введите язык (русский - ru, английский - en): ")
user_shift = int(input("Введите шаг сдвига: "))
user_text = input("Введите текст: ")

if user_lang == "ru":
    alphabet = ru
elif user_lang == "en":
    alphabet = en
else:
    print("Неверный выбор языка.")
    exit()

if direction == "1":
    print("Зашифрованный текст:", text_caesar(alphabet, user_text, user_shift))
elif direction == "2":
    a = input("Известно ли кол-во шагов (y/n): ")
    if a == 'y':
        print("Расшифрованный текст:", decrypt_text_caesar(alphabet, user_text, user_shift))
    else:
        print("Перебор всех возможных сдвигов:")
        for i in range(0, len(alphabet)):
            print(f"Сдвиг {i}: {decrypt_text_caesar(alphabet, user_text, i)}")
else:
    print("Неверный выбор действия.")

