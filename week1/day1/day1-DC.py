number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)

user_string = input("Enter a word: ")

result = ""

for char in user_string:
    if result == "" or char != result[-1]:
        result += char

print(result)
