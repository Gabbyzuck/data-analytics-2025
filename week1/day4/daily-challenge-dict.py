#Challenge 1
user_word = input('Enter a word: ')
letter_dict = {}
for index, letter in enumerate(user_word):
    if letter not in letter_dict:
        letter_dict[letter] = [index]
    else:
        letter_dict[letter].append(index)
print(letter_dict)

#Challenge 2
items_purchase = {
    'Tuna': '$5',
    'Chapstick': '$3',
    'Shampoo': '$10',
    'Blueberries': '$85'
}

print(items_purchase.keys())

print(sorted(items_purchase.keys()))

wallet = 0
can_buy = []

for item, price in items_purchase.items():
    item_amount = float(price.replace('$',''))

    if item_amount <= wallet:
        can_buy.append(item)

if can_buy:
    print(can_buy)
else:
    print('Nothing')