import sys
import re
import argparse
from cipher import Cipher


def main():
    parser = argparse.ArgumentParser(
        description="Encode or decode text with a simple substitution cipher"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-e",
        "--encode",
        action="store_true",
        help="Run in encode mode to encode a string",
    )
    group.add_argument(
        "-d",
        "--decode",
        action="store_true",
        help="Run in decode mode to decode a string",
    )
    args = parser.parse_args()

    if args.encode:
        print("Encoding")
        verb = "encode"
        f = encode
    elif args.decode:
        print("Decoding")
        verb = "decode"
        f = decode
    else:
        sys.exit("Unrecognized argument")

    phrase = input(f"What do you want to {verb}? ")
    if not validate(phrase):
        sys.exit("Entered phrase must only contain alpha characters or spaces")

    try:
        shift = int(input("Shift value: "))
    except ValueError:
        sys.exit("Shift value must be an integer")

    processed_phrase = f(phrase, shift)

    print(phrase.upper())
    print(processed_phrase)


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
