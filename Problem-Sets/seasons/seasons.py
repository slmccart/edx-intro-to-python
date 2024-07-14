from datetime import date
import sys
import inflect


def main():
    # Prompt for date in YYYY-MM-DD format
    dob_string = input("Date of Birth: ")

    try:
        dob = convert_input(dob_string)
    except:
        sys.exit("Invalid Date")

    minutes = time_delta_in_minutes(dob, date.today())

    print(convert_minutes_to_words(minutes))

def convert_input(input):
    try:
        return date.fromisoformat(input)
    except ValueError:
        raise ValueError("Invalid Date")

def time_delta_in_minutes(start, end):
    delta = end - start
    return delta.days * 24 * 60

def convert_minutes_to_words(minutes):
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
