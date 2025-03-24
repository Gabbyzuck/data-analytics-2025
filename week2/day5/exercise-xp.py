# # Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        print(self.__dict__) 

    def sit(self):
        print(f"{self.name} is sitting")

    def old(self):
        print(f"{self.name} is {self.age} years old")

    def lazy(self):
        print(f"The lazy cat named {self.name}")

ginger = Cat("Ginger", 3)
ginger.sit()
ginger.old()
ginger.lazy()


def old_cat(all_cats):
        oldest = max(all_cats, key=lambda cat: cat.age)
        print(f"The oldest cat is {oldest.name} and is {oldest.age} years old.")

cat1 = Cat("Ginger", 3)
cat2 = Cat("Whiskey", 5)
cat3 = Cat("Luna", 7)

cats = [cat1, cat2, cat3]
old_cat(cats)

# # Exercise 2: Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high.")

davids_dog = Dog("Rex", 50)

davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog.")
else:
    print(f"{sarahs_dog.name} is the bigger dog")

# Exercise 3: Who's The Song Producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
   
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4: Afternoon At The Zoom
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animal_groups = {}
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
   
    def get_animals(self):
        print(self.animals)
    
    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)
        print(grouped_animals)
    
    def get_groups(self):
        for letter, group in self.animal_groups.items():
            print(f"{letter}: {group}")

zoo = Zoo("Zoo")

zoo.add_animal("Monkey")
zoo.add_animal("Penguin")
zoo.add_animal("Rhino")
zoo.add_animal("Racoon")

zoo.get_animals()

zoo.sort_animals()  
zoo.get_groups() 

new_york_zoo = Zoo("New York Zoo")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.get_animals()
new_york_zoo.sort_animals()
new_york_zoo.get_groups()


