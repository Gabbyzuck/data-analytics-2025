# #Exercise 1: Convert Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for item in zip(keys, values):
    print(item)

# Exercise 2 : Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for name, age in family.items():
    if age < 3:
        cost = 0
        print(f"{name}: Free'")
    elif age < 12:
        cost = 10
        print(f"{name}: $10")
    else:
        cost = 15
        print(f"{name}: $15")

    total_cost += cost

print(f'Total Cost: ${total_cost}')

family = {}

while True:
    name = input('Enter a name of your family member or type "done" to quit: ')
    if name.lower() == "done":
        break
    age = int(input(f'Enter the age of {name}: '))
    family[name] = age

    total_cost = 0

    if age < 3:
        cost = 0
        print(f"{name}: Free")
    elif age <= 12:
        cost = 10
        print(f"{name}: $10")
    else:
        cost = 15
        print(f"{name}: $15")

total_cost += cost

print(f'Total Cost: ${total_cost}')

# #Exercise 3: Zara
brand_dict = {
    'name' : 'Zara', 
    'creation_date' : '1975', 
    'creator_name' : 'Amancio Ortega Gaona', 
    'type_of_clothes':[
        'men', 
        'women', 
        'children', 
        'home',
     ],
    'international_competitors':[
        'Gap', 
        'H&M', 
        'Benetton', 
     ],
    'number_stores' : 7000,
    'major_color':{
        'France' : 'blue', 
        'Spain' : 'red', 
        'US':[
            'pink', 
            'green'
        ]
    }
    }

brand_dict['number_stores'] = 2
print(brand_dict)

type_of_clothes = brand_dict['type_of_clothes']
for values in type_of_clothes:
    print(f"Zara has a client base that shops for {values}")

brand_dict['country_creation'] = 'Spain'
print(brand_dict)

if 'international_competitors' in brand_dict:
    brand_dict['international_competitors'].append('Desigual')
    print(brand_dict)

creation_date = brand_dict.pop('creation_date')
print(brand_dict)

if 'international_competitors' in brand_dict:
    print(brand_dict['international_competitors'][-1])
else:
    print('international_competitors key not found')

print(len(brand_dict))

print(brand_dict.keys())

more_on_zara = {
    'creation_date' : 1975,
    'number_stores': 10000
}

brand_dict.update(more_on_zara)
print(brand_dict)

print(brand_dict['number_stores'])

#Exercise 4: Disney Characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#1/
disney_users_A = {}
for index, name in enumerate(users):
    disney_users_A[name] = index
print(disney_users_A)

#2/
disney_users_B = dict(zip(disney_users_A.values(), disney_users_A.keys()))
print(disney_users_B)

#3/
sorted_users = {key: disney_users_A[key] for key in sorted(disney_users_A.keys())}
print(sorted_users)

#4/a
i_disney_users = {user: index for index, user in enumerate(users) if 'i' in user}
print(i_disney_users)
#4/b
mp_disney_users = {user: index for index, user in enumerate(users) if user[0] in ['M','P']} #[] creates list
print(mp_disney_users)