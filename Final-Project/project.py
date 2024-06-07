import sys
from cipher import Cipher


def main():
    phrase = input("What do you want to encode? ").upper()
    # Check for non-alpha
    if not phrase.isalpha():
        sys.exit("Only alphabetic characters are allowed")

    try:
        shift = int(input("Shift value: "))
    except ValueError:
        sys.exit("Shift value must be an integer")

    print(encode(phrase, shift))


def encode(s, shift):
    cipher = Cipher(shift)
    return cipher.encode(s)


if __name__ == "__main__":
    main()
