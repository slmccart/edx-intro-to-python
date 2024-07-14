def main():
    while True:
        try:
            value = convert(input("Fraction: "))
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

    print(gauge(value))

def convert(fraction):
    try:
        x, sep, y = fraction.partition("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError

    except ValueError:
        raise ValueError
    else:
        return round((x/y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
