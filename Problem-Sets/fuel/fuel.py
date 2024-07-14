def main():
    fraction = get_fraction()

    if fraction <= .01:
        print("E")
    elif fraction >= .99:
        print("F")
    else:
        print(f"{round(fraction * 100)}%")

def get_fraction():
    while True:
        str = input("Fraction: ")

        try:
            x, sep, y = str.partition("/")
            x = int(x)
            y = int(y)

            if x > y:
                continue

            return x/y
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
