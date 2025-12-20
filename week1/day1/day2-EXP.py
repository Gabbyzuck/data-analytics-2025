# Exercise 1
my_fav_numbers = {3, 7, 21}

# Add two numbers
my_fav_numbers.add(10)
my_fav_numbers.add(42)

# Remove one number (sets are unordered, so remove any one)
my_fav_numbers.remove(42)

friend_fav_numbers = {5, 7, 99}

# Union of sets
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("Our favorite numbers:", our_fav_numbers)


# Exercise 2
numbers = (1, 2, 3)

# Tuples are immutable, so this is NOT allowed:
# numbers.append(4)  

print("Tuples cannot be modified after creation.")

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

print("Apples count:", basket.count("Apples"))

basket.clear()
print("Final basket:", basket)

# Exercise 4
# A float is a number with a decimal point, an integer is a whole number.

numbers = []

for i in range(1, 6):
    numbers.append(i)
    numbers.append(i + 0.5)

numbers = numbers[1:]  # remove the first extra integer
print(numbers)

# Exercise 5
for i in range(1, 21):
    print(i)

print("Even index numbers:")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 6
while True:
    name = input("Enter your name: ")

    if name.isdigit() or len(name) < 3:
        print("Invalid name, try again.")
    else:
        print("Thank you")
        break

# Exercise 7
fav_fruits = input("Enter your favorite fruits (separated by spaces): ").split()

fruit = input("Enter a fruit name: ")

if fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8
toppings = []
price = 10

while True:
    topping = input("Enter a pizza topping (or 'quit'): ")

    if topping == "quit":
        break

    toppings.append(topping)
    price += 2.5
    print(f"Adding {topping} to your pizza.")

print("Your pizza toppings:", toppings)
print(f"Total price: ${price}")

# Exercise 9
ages = input("Enter ages (separated by spaces): ").split()
total_cost = 0

for age in ages:
    age = int(age)

    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print("Total ticket cost:", total_cost)

# Bonus
ages = input("Enter ages of attendees: ").split()
allowed = []

for age in ages:
    age = int(age)
    if 16 <= age <= 21:
        allowed.append(age)

print("Allowed attendees:", allowed)

