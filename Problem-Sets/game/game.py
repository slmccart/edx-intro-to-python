import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
        else:
            break
    except ValueError:
        continue

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess == answer:
        print("Just right!")
        sys.exit()
    elif guess < answer:
        print("Too small!")
        continue
    else:
        print("Too large!")
        continue
