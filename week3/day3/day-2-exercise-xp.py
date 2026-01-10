# ----- Base Classes (given) -----

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return sounds


class Chartreux(Cat):
    def sing(self, sounds):
        return sounds


# ----- Step 1: Create Siamese Class -----

class Siamese(Cat):
    pass   # No special behavior for now


# ----- Step 2: Create Cat Instances -----

bengal = Bengal("Leo", 3)
chartreux = Chartreux("Milo", 5)
siamese = Siamese("Luna", 2)

all_cats = [bengal, chartreux, siamese]

# ----- Step 3: Create Pets Instance -----

sara_pets = Pets(all_cats)

# ----- Step 4: Take Cats for a Walk -----

sara_pets.walk()

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"


# ----- Step 2: Create Dog Instances -----

dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 4, 28)

# ----- Step 3: Test Dog Methods -----

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

import random
from dog import Dog   # import from previous exercise


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]
        for dog in args:
            dog_names.append(dog.name)
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet")


# ----- Step 3: Test PetDog Methods -----

dog1 = PetDog("Fido", 2, 10)
dog2 = PetDog("Buddy", 3, 12)

dog1.train()
dog1.play(dog2)
dog1.do_a_trick()
dog2.do_a_trick()

# ----- Step 1: Person Class -----

class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


# ----- Step 2: Family Class -----

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(
                        f"You are over 18, your parents Jane and John accept "
                        f"that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")


# ----- Testing -----

my_family = Family("Smith")

my_family.born("Anna", 17)
my_family.born("James", 20)

my_family.family_presentation()
my_family.check_majority("Anna")
my_family.check_majority("James")
