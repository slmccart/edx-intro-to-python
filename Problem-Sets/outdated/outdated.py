def main():
    while True:
        date_string = input("Date: ")

        try:
            if date_string.find("/") != -1:
                month, day, year = split_slash_delimited_date(date_string)
            elif date_string.find(" ") != -1:
                month, day, year = split_space_delimited_date(date_string)
        except ValueError:
            continue

        if month > 12 or int(day) > 31:
            continue
        else:
            break

    print(year, f"{month:02}", f"{day:02}", sep="-")

def split_slash_delimited_date(date):
    #Split MONTH/DAY/YEAR formatted strings
    month, day, year = date.split(sep="/")

    try:
        #Convert to integers
        return [int(month), int(day), int(year)]
    except ValueError:
        raise ValueError("Incorrect date format provided")

def split_space_delimited_date(date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    #Split MONTH DAY, YEAR formatted strings
    month, day, year = date.split(sep=" ")

    if day.endswith(","):
        #Trim comma from day
        day = day.strip(",")
    else:
        raise ValueError("Invalid format provided")

    try:
        #Convert textual month to numeric
        month = months.index(month) + 1
    except ValueError:
        raise ValueError("Invalid Month provided")
    else:
        #Convert to integers
        return [month, int(day), int(year)]

main()
