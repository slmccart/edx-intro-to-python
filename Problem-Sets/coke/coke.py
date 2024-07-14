def main():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)
        amount_due -= get_valid_coin()

    print("Change Owed:", abs(amount_due))

def get_valid_coin():
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        return coin
    else:
        return 0

main()
