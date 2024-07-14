def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return correct_number_of_characters(s) and starts_with_two_letters(s) and no_numbers_in_the_middle(s) and no_punctuation(s)

def starts_with_two_letters(s):
    return s[:2].isalpha()

def correct_number_of_characters(s):
    return 2 <= len(s) <= 6

def no_numbers_in_the_middle(s):
    for i in range(len(s)):
        if s[i].isdecimal():
            if s[i] == "0":
                return False
            else:
                return s[i+1:].isdecimal()
    return True

def no_punctuation(s):
    return s.isalnum()

if __name__ == "__main__":
    main()
