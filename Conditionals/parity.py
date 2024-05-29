def is_even(n):
    return n % 2 == 0

def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

main()