import sys
import csv

def main():
    if len(sys.argv[1:]) != 2:
        sys.exit("Incorrect number of command-line arguments")

    input, output = sys.argv[1:]

    students = []
    try:
        with open(input) as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                last, first = row["name"].split(",")
                students.append({"first": first.lstrip(), "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"File not found: {input}")

    with open(output, "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)

if __name__ == "__main__":
    main()
