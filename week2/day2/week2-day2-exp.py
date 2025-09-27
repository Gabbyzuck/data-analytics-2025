# # Exercise 1: What Are You Learning?
# def display_message():
#     print(message)

# message = ('I am learning about functions in Python.')
# # print(message)

# display_message()

# # Exercise 2: What’s Your Favorite Book?
# def favorite_book(title):
#     print(f"One of my favorite books is '{title}'.")

# title = 'Tender is the Night'

# favorite_book(title)

# # Exercise 3: Some Geography
# def describe_city(city, country='Unknown'):
#     print(f"{city} is in {country}.")

# describe_city('Reykjavik', 'Iceland')
# describe_city('Paris')

# # Exercise 4: Random
# import random

# def check_number(user_num):
#     rand_num = random.randint(1, 100)
#     if user_num == rand_num:
#         print("Success!")
#     else:
#         print("Fail :(")
#     print(f"Your number: {user_num}, Random number: {rand_num}")

# user_input = int(input("Enter a number between 1 and 100: "))

# check_number(user_input)

# Exercise 5: Let’s Create Some Personalized Shirts!
# def make_shirt(size="large", text="I love Python"):
#     print(f"The shirt size is {size} and the text is '{text}'")

# make_shirt()  
# make_shirt(size="medium")  
# make_shirt(size="small", text="Hello World")

# Exercise 6: Magicians…
magician_names = [
    "Harry Houdini", 
    "David Blaine", 
    "Criss Angel"
]

def show_magicians(names):
    for name in names:
        print(name)

show_magicians(magician_names)

def make_great(names):
    for name in names:
        print(f"{name} The Great")

make_great(magician_names)
show_magicians(magician_names)

# # Exercise 7: Temperature Advice
import random

def get_random_temp(season):
    if season == "Winter":
        return random.uniform(-10, 5)   
    elif season == "Spring":
        return random.uniform(5, 20)    
    elif season == "Summer":
        return random.uniform(20, 35)   
    elif season == "Autumn":
        return random.uniform(5, 20)    
    else:
        return random.uniform(-10, 35)  

def main():
    month = int(input("Enter the month number (1-12): "))

    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    elif month in [9, 10, 11]:
        season = "Autumn"
    else:
        print("Invalid month! Defaulting to random temperature.")
        season = None

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp:.1f}°C.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23: 
        print("Nice weather")
    elif 23 <= temp < 32:
        print("A bit warm, stay hydrated.") 
    else: 
        print("It’s really hot! Stay cool.")

main()






