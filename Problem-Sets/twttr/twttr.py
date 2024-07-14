def main():
    prompt = input("Input: ")
    print("Output:", remove_vowels(prompt))

def remove_vowels(str):
    return_val = ""

    for char in str:
        if not is_vowel(char):
            return_val += char

    return return_val

def is_vowel(char):
    char = char.lower()
    return char == "a" or char == "e" or char == "i" or char == "o" or char == "u"

main()
