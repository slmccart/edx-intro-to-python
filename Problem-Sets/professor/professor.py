import random


def main():
    level = get_level()

    correct_answers = 0

    for _ in range(10):
        incorrect_guesses = 0

        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        while True:
            if incorrect_guesses == 3:
                print(f"{x} + {y} = {answer}")
                break
            else:
                try:
                    guess = int(input(f"{x} + {y} = "))
                except ValueError:
                    incorrect_guesses += 1
                    print("EEE")
                    continue

                if answer == guess:
                    correct_answers += 1
                    break
                else:
                    incorrect_guesses += 1
                    print("EEE")

    print(f"Score: {correct_answers}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    # Can't figure out how to get low_limit = 0, so force it for level 1
    if level == 1:
        low_limit = 0
    else:
        low_limit = 10**(level - 1)
    high_limit = (10**level) - 1

    return random.randint(low_limit, high_limit)


if __name__ == "__main__":
    main()
