# f = open('output.txt', 'w')
# for i in range(10):
#     f.write("this is line: %i\n"%i)
# f.close()

# # Same as
# with open('output.txt', 'w') as f:
#     for i in range(11, 20):
#        f.write("this is line: %i\n"%i)

# with open('names.txt', 'r') as f:
#     text = f.read()
#     print(text)

# with open('names.txt', 'r') as f:
#     text = f.read()[0:5]
#     print(text)

# sw = {'Darth': 0, 'Luke':, 0, 'Lea': 0}
# with open('names.txt', 'r') as f:
#     for i in f.readlines():
#         sw[i.rstrip()] += 1
# print(sw)

# new_names = [] #need empty list
# with open('names.txt', 'r+') as f:
#     names = f.readlines()
#     for name in names:
#         if name.rstrip() == 'Luke':
#             new_names.append('Luke Skywalker/n')
#         else:
#             new_names.append(name) #otherwise, name just stays name
#     for name in new_names:
#         f.write(name) #writes over names
# print(new_names)

# import json

# my_family = {
#     "parents":['Beth', 'Jerry'],
#     "children":['Summer', 'Morty']
# }

# json_file = "my_file.json"

# with open(json_file, 'w') as file_obj:
#     json.dump(my_family, file_obj, indent = 2, sort_keys=True)

# import requests 

# current_location = requests.get("http://api.open-notify.org/iss-now.json")

# print(current_location.json())

#API
# chuck_url = 'http://api.chuck.io?query=dev'
# req = requests.get(chuck_url)
# info = req.json()
# joke = info['value']
# print(joke)