import sys
from cipher import Cipher


def main():
    phrase = input("What do you want to encode? ")
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


def encode(s, shift):
    encoded_phrase = ""
    cipher = Cipher(shift)

    words = s.upper().split(" ")
    for word in words:
        # Check for non-alpha
        if not word.isalpha():
            raise ValueError
        else:
            encoded_phrase += cipher.encode(word) + " "

    return encoded_phrase.strip()


if __name__ == "__main__":
    main()
