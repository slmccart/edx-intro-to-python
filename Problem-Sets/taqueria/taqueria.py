def main():
    total = 0
    while True:
        try:
            total += prompt_item()
            print("Total: $", "{:.2f}".format(total), sep="")
        except EOFError:
            print()
            break

def prompt_item():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        key = input("Item: ").title()

        try:
            return menu[key]
        except KeyError:
            pass

main()
