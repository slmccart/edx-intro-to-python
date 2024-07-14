def convert(input):
    modified = input.replace(":)","🙂")
    modified = modified.replace(":(","🙁")
    return modified

def main():
    prompt = input("What would you like to say? ")
    print(convert(prompt))

main()
