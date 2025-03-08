import random

def number_guessing_game(): #(): defines a function
    random_number = random.randint(1, 100)
    max_attempts = 7

    for i in range(max_attempts):
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {random_number}.")

number_guessing_game() #calls the function
