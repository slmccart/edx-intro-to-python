import sys
from cipher import Cipher


def main():
    phrase = input("What do you want to encode? ").upper()
    # Check for non-alpha
    if not phrase.isalpha():
        sys.exit("Only alphabetic characters are allowed")
    shift = int(input("Shift value: "))

    print(encode(phrase, shift))


def encode(s, shift):
    cipher = Cipher(shift)
    return cipher.encode(s)


if __name__ == "__main__":
    main()
