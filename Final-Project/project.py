import sys
import re
from cipher import Cipher


def main():
    phrase = input("What do you want to encode? ")
    if not validate(phrase):
        sys.exit("Entered phrase must only contain alpha characters or spaces")

    try:
        shift = int(input("Shift value: "))
    except ValueError:
        sys.exit("Shift value must be an integer")

    try:
        encoded_phrase = encode(phrase, shift)
    except ValueError:
        sys.exit("Entered phrase must only contain alpha characters or spaces")

    print(phrase.upper())
    print(encoded_phrase)


def validate(s):
    return re.match(r"^[a-zA-Z ]+$", s)


def __process(s, f):
    processed_phrase = ""

    words = s.upper().split(" ")
    processed_words = map(f, words)

    for word in processed_words:
        processed_phrase += word + " "
    return processed_phrase.strip()


def encode(s, shift):
    cipher = Cipher(shift)
    return __process(s, cipher.encode)


def decode(s, original_shift):
    cipher = Cipher(original_shift)
    return __process(s, cipher.decode)


if __name__ == "__main__":
    main()
