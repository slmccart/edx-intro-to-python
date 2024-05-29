def main():
    print_column(3)
    print_row(4, "?")
    print_square(3)

def print_square(size):
    for row in range(size):
        print_row(size, "#")

def print_row(width, char):
    print(char * width)

def print_column(height):
    for _ in range(height):
        print("#")

main()