# class Circle:
#     color = "red"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#        return Circle.color

# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)

# class Man():
#     sex = "Male"

#     @staticmethod
#     def get_nicknames():
#         return ["Bro", "Dude", "Buddy"]

# # alex = Man()

# # print(alex.get_nicknames())

# class MyClass:
#   def __init__(self, first_name, last_name):
#     self.__first_name = first_name
#     self.__last_name = last_name

#   @property
#   def email(self): 
#     return f"{self.__first_name}.{self.__last_name}@gmail.com"

#   @email.setter
#   def email(self, name): 
#     self.__first_name = name

#   @property 
#   def get_firstname(self):
#     return self.__first_name

# newClass = MyClass("John", "Doe")
# newClass.email = "Sarah"
# print(newClass.email)

# print(newClass.get_firstname)

# class Person:

#     used_names = set()

#     def __init__(self, name, age):
#         if name in self.used_names:
#             name = input("That name is taken. Enter another name: ")

#         self.name = name
#         self.age = age
#         self.used_names.add(name)

#     @classmethod
#     def fromYear(cls, name, birth_year):
#         THIS_YEAR = 2020
#         return cls(name, THIS_YEAR - birth_year)

#     @property
#     def professional_name(self):
#         return "Mr " + self.name

# sharon = Person("Sharon", 29)
# markus = Person("Markus", 40)

# # Person.fromYear("Sharone", 1996)

# # print(markus.professional_name)

# class MyClass():
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print(f"Value of object : {object_1.get_val()}")
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print(f"Value of object : {object_2.get_val()}")
# print(MyClass.get_count())



# Dunder method
# class Ilan:
#     def __init__(self, coolness_level):
#         self.coolness_level = coolness_level
# Ilans = Ilan(8)

# print(Ilans) #prints memory address - it's useless

# class Ilan:
#     def __init__(self, coolness_level):
#         self.coolness_level = coolness_level

#     def __repr__(self):
#         return f"This Ilan has a coolness value of {self.coolness_level}"

#     def __call__(self):
#         for i in range(self.coolness_level):
#             print(f"I'm cool {1 + 1} times")
    
#     def __add__(self,*args):
#         self.coolness_level += sum(args)
#         print("coolness level updated")
#         return self.coolness_level


# # Ilans = Ilan(8)

# Iland + 5

# Ilans()

# print(dir(list))    



# class Person:
#   def __init__(self, name, lastName):
#       self.name = name
#       self.lastName = lastName


# #Here we overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'

#   def __repr__(self):

# # We can write whatever we want inside this method, but we have to return an object.

#       return f"{self.__class__.__name__} : {self.name} {self.lastName}"

#   def __add__(self,other):
#     name = self.name[0] + other.name[1:]
#     lastname = other.lastName
#     return Person(name,lastname)

# father = Person('John', 'Snow')
# mother = Person('Kaleesi', 'MotherOfDragons')
# # using the __add__() method
# dragonChild = father + mother 

# print(dragonChild)
# # >>Person : Jaleesi MotherOfDragons

class PrintList():

    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__())