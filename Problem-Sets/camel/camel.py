def main():
    prompt = input("camelCase: ").strip()

    print("snake_case: " + to_snake(prompt))

def to_snake(str):
    return_val = ""

    for char in str:
        if char.isupper():
            return_val += "_"
            return_val += char.lower()
        else:
            return_val += char

    return return_val.lstrip("_")

main()
