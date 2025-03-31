### 1 ###
# description = "strings are ..."
# print(description.upper())
# ### 2 ###
# print(description.replace("are", "is"))
# ### 3 ###
# print(description.split()[0])
# my_age = 411
# 123879 + my_age
# print(int("12") + 13)
# bank_balance = '33000'
# print(type(bank_balance))
# print(int(bank_balance))
# phone_number = 532287514
# print(type(phone_number))
# print(str(phone_number))
# first_name = "Gabby"
# last_name = "Zuckerman"
# print(first_name + " " + last_name)
# print(first_name, last_name)
# print("The cow says, \"moo\"")
# name = "Alice"
# age = "30"
# city = "New York"
# print(f"Hello, {name}! You are {age} years old and live in {city}.")
# hobby = input("What is your favorite hobby? ")
# next_week = input("What do you want to do next week? ")
# print(f"You want to {next_week} next week.")
# number = int(input("Input a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")

# ch = "chair"
# print(ch[0])
# # my_list[1:] means you have item 1 and all items to the end of the list
# my_buddy = "Ilan" 
# my_buddy[0:3]
# print(my_buddy[0:3])
# my_students = ["Alice", "Bob", "Jorge", "Lisa", "Sue"]
# print(my_students[0]) # index numbers MUST be in []
# my_students [0] = "alex"
# print(my_students)
# my_students[0:3] = [1,2,3]
# print(my_students)
# my_students.append("Alice")
# print(my_students) #append adds values to the end of the list
# my_students.remove(1)
# print(my_students)
# my_students.pop(0)
# print(my_students)
data_people = ("sam", "sharon", "gabby")
# full_stack = ("alex", "daniel", "ilan")
# whole_class = data_people + full_stack
# print(whole_class)
# print(len(data_people))

### issues ###
# list1 = [5, 10, 15, 20, 25, 50, 20]
# twenty_index = list1.index(20)
# list1(twenty_index) = 200
# print(list1)

# a_tuple = (10, 20, 30, 40)
# print(a_tuple[0])
# print(a_tuple[1])
# print(a_tuple[2])
# print(a_tuple[3])

# print(set(data_people))
# print(list(data_people))

# to replace value in list, variable[index] = new value

# add colon at the end before you indent print (because its a conditional)
# for num in range(10,22):
# #     print(num)
# for num in range(0,11,2):
#     print(num)
# this_list = [1,2,3,4,5]
# print(sum(this_list))

# user_number = int(input("Input a number: "))
# for number in range(11):
#     print(user_number * number)
    ### OR ###
# num = int(input("Input a number: "))
# print(f"Multiplication Table of {num}:")
# for i in range(1,21):
#     print(f"{num} x {i} = {num * i}")


# a_number = 1
# while a_number < 12:
#     print(a_number)
#     a_number += 1
# #     # to cancel operation, CTRL + c
# i = 1
# while i < 11:
#     print(i)
#     i += 1
#     ### OR ###
# t = 1
# while t<=10:
#     print(t)
#     t += 1

# g = 0
# while g < 12:
#         g += 1

#     if g == 7:
#         continue
#         print(g)

#1
# user_string = input("type a 10 char long string: ")
# if len(user_string) < 10:
#     print("string not long enough")
# elif len(user_string) > 10:
#     print("string too long")
# else:
#     print("perfect string")
# #2
# print(user_string[0])
# print(user_string[-1])
# #3
# for char in user_string:
#     print(user_string[1])
#     char += 1

#Challenge 2
string = input("Enter a word: ")
char_list = list(string)

1 = 
while i < len(char_list):
    if i == len(char_list) - 1:
        break
    if char_list[i] == char_list[i + 1]:
        char_list.pop(i + 1)
    else:
        i += 1

print("".join(char_list))

