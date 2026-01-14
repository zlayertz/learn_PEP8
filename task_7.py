class Animal:
    def __init__(self):
        self.weight = None
        self.age = None
        self.name = None

    def init(self, name=None, age=None, weight=None):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):
        if self.weight is not None:
            self.weight += food
        return self.weight

    def info(self):
        print(f"{self.name}, {self.age} years, {self.weight} kg")


def meow():
    print("MEOW!")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.breed = None

    def init(self, name=None, age=None, weight=None, breed=None):
        super().init(name, age, weight)
        self.breed = breed
