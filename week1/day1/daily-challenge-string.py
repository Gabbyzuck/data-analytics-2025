#1
user_string = input('Enter a 10 character string: ')
if len(user_string) < 10:
    print('string not long enough')
elif len(user_string) > 10:
    print('string too long')
else:
    print('perfect string')

#2
print(user_string[0])
print(user_string[-1])

#3
string = ''
for character in user_string:
    string += character
    print(string)
  