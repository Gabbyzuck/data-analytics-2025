# class Animal():
#     def __init__(self, name, num_legs, sound):
#         self.name = name
#         self.num_legs = num_legs
#         self.sound = sound
    
#     def make_sound(self):
#         print(f'I go {self.sound}')

#     def fetch(self):
#         print('This animal goes fetch')

# class Dog(Animal):
#     def fetch(self):
#         print('I am a dog and I go fetch sticks')

# prince = Dog('Prince', 4, 'Waf')
# # prince.make_sound()
# prince.fetch()

# tippy = Dog('Tippy', 3, 'Woof')
# # tippy.make_sound()
# tippy.fetch()

# print(tippy.num_legs)

# ralph = Animal('Ralph', 2, 'squak')
# # ralph.make_sound()
# ralph.fetch()

# Exercise 
# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)


# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)  #Did not run grow function at this point

# nc.grow()

# print(nc.diameter)

# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         super().__init__(type, number_legs, sound)
#         # Or : Animal.__init__(self,type, number_legs, sound)
#         self.fetch_ball = fetch_ball

# barky = Dog('Dog', 4, 'Bark', True)
# print(barky.number_legs)

# class MyClass:
#     def func(self):
#         print("I'm being called from the Parent class")


# class ChildClass(MyClass):
#     def func(self):
#         print("I'm actually being called from the Child class")
#         print("But...")
#         # Calling the `func()` method from the Parent class.
#         super().func()

# my_instance_2 = ChildClass()
# my_instance_2.func()

# class Door:
#     def __init__(self, is_opened = True):
#         self.is_opened = is_opened
#     def open_door(self):
#         self.is_opened = True
#     def closed_door(self):
#         self.is_opened = False

# class BlockedDoor(Door):
#     def __init__(self):
#         super().__init__(False)
#     def open_door(self):
#         raise ValueError('A blocked door cannot be opened')
#     def closed_door(self):
#         return super().closed_door
# my_door = BlockedDoor()
# my_door.open_door()

# def age():
#     user_age = input("How old are you?\n>>> ")
#     #######
#     try:
#         user_age = int(user_age)
#         print("I AM AFTER USER_AGE")
#     except:
#         print("Your age is not a real age")
#         user_age = 0
#     #######
#     print(f"Next year, you will be {user_age+1} years old")

# age()

# # How old are you?
# # >>> 3weqf
# # Your age is not a real age
# # Next year, you will be 1 year old

valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:
        userage = int(userage)
        valid_flag = True
    except:
        print("Please enter a real age")

print("Next year, your age will be",userage+1)