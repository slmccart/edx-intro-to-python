def f(*args, **kwargs):
    print("Named:", kwargs)
    # print("Positional:", args)


f(galleons=100, sickles=50, knuts=25)

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(**coins), "Knuts")
# # Unpacks to the equivalent of total(galleons=100, sickles=50, knuts=25)
