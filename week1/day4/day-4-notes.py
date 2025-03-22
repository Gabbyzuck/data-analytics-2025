# shirts = [
# {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
# },
# {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
# },
# {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
# },
# ]
# print(shirts[1]['price'])

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict["class"]["student"]["marks"]["history"])

# del variable[value] deletes the value in the variable

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# keys_to_remove = ["name", "salary"]
# del sample_dict["name"]
# del sample_dict["salary"]
# print(sample_dict)


# # range(0,10)
# # print(list(range(1,11,2)))

# print(list(enumerate('hello kitty')))
# To enumerate, convert to list first

# for i in range(1,10):
#     print(i)
#     if i == 9:
#         break
# else:
#     print('The for loop is over')

# for letter in 'Leonardo':
#     if letter == 'a':
#         continue  #continue skips the current iteration. In this case, skips the letter 'a'
#     print(letter, end='')

# List Comprehension
# my_number = '1234'

# # for num in my_number:
# #     num

# my_list = [int(num) * 2 for num in my_number] #1st variable will be added to list. 2nd variable is what will be variable in loop
# print(my_list)

# my_list = []
# for num in my_number:
#     my_list.append(int(num) * 2)
# print(my_list)

#Time Complexity = Big O Notation
# my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]

# print(my_list)

family_age = {'Lea': 12, 'Mark': 25, 'George': 50}

new_year = 1

new_family_age = {name: age+new_year for (name, age) in family_age.items()}

print(new_family_age)