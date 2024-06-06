class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if house not in valid_houses:
            raise ValueError(f"house must be one of: {valid_houses}")
        self._house = house


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
