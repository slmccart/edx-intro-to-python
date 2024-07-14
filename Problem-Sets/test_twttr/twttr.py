def main():
    prompt = input("Input: ")
    print("Output:", shorten(prompt))


def shorten(word):
    return_val = ""

    for char in word:
        if not char in "AEIOUaeiou":
            return_val += char

    return return_val


if __name__ == "__main__":
    main()
