import sys


def main():
    phrase = input("What do you want to encode? ").upper()
    # Check for non-alpha
    if not phrase.isalpha():
        sys.exit("Only alphabetic characters are allowed")
    shift = int(input("Shift value: "))

    print(encode(phrase, shift))


def encode(s, shift):
    """Encode a string using a substituion cypher, shifting each character by the value of shift"""
    # A = 65
    low_val = 65
    # Z = 90
    high_val = 90

    encoded_string = ""
    for char in s:
        int_val = ord(char) + shift
        if int_val < low_val:
            delta = low_val - int_val
            int_val = (high_val + 1) - delta
        elif int_val > high_val:
            delta = int_val - high_val
            int_val = (low_val - 1) + delta

        encoded_string += chr(int_val)

    return encoded_string


if __name__ == "__main__":
    main()
