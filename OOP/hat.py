import random


class Hat:
    def __init__(self) -> None:
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)


def main():
    hat = Hat()
    hat.sort("Harry")


if __name__ == "__main__":
    main()
