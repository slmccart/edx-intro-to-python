import validators

def main():
    if validators.email(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")

main()
