import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
print(cards)
random.shuffle(cards)
print(cards)