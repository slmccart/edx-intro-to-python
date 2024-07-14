def main():
    grocery_list = {}

    while True:
        try:
            item = get_grocery_item()
        except EOFError:
            print()
            break

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    #Sort and print grocery list
    sorted_keys = sorted(list(grocery_list))

    for key in sorted_keys:
        print(grocery_list[key], key)

def get_grocery_item():
    return input().upper()

main()
