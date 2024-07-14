import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv[1:]) != 1:
        sys.exit("Call with exactly one command-line argument")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Must specify a .csv file")

    menu = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not find file: {filename}")

    print(tabulate(menu, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
