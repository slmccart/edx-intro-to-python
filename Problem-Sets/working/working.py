import re
import sys


def main():
    print(convert(input("Hours: ")))

# Converts string in one of the following formats to 24-hour format (i.e. 9:00 to 17:00):
#. 1) 9:00 AM to 5:00 PM
#. 2) 9 AM to 5 PM
def convert(s):
    if matches := re.search(r"^(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)$", s):
        start_hours, start_minutes, start_am_pm, end_hours, end_minutes, end_am_pm = matches.groups()


    elif matches := re.search(r"^(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)$", s):
        start_hours, start_am_pm, end_hours, end_am_pm = matches.groups()
        start_minutes = "0"
        end_minutes = "0"
    else:
        raise ValueError(f"Unknown string format: {s}")

    start_hours = int(start_hours)
    end_hours = int(end_hours)
    start_minutes = int(start_minutes)
    end_minutes = int(end_minutes)

    if start_minutes > 59 or end_minutes > 59:
        raise ValueError

    if start_hours > 12:
        raise ValueError("Starting hours must be less than 12")

    if end_hours > 12:
        raise ValueError("Ending hours must be less than 12")

    if start_hours == 12:
        # Special handling for 12 AM and 12 PM
        if start_am_pm == "AM":
            start_hours = 0
    elif start_am_pm == "PM":
        start_hours += 12

    if end_hours == 12:
        # Special handling for 12 AM and 12 PM
        if end_am_pm == "AM":
            end_hours = 0
    elif end_am_pm == "PM":
        end_hours += 12

    return f"{start_hours:02}:{start_minutes:02} to {end_hours:02}:{end_minutes:02}"


if __name__ == "__main__":
    main()
