import sys

def main():

    if len(sys.argv[1:]) != 1:
        sys.exit("Call with exactly one command-line argument")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Must specify a .py file")

    lines = 0
    try:
        with open(filename) as file:
            for line in file:
                if line.isspace() or line.lstrip().startswith("#"):
                    continue
                else:
                    lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(lines)

if __name__ == "__main__":
    main()
