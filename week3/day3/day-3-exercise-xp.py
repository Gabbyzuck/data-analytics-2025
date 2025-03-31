#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __add__(self, other):
        try:
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        except AttributeError:
            return Currency(self.currency, self.amount + other)

    def __iadd__(self, other):
        try:
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        except AttributeError:
            self.amount += other
        return self
    
    def __eq__(self, other):
        try:
            return self.currency == other.currency and self.amount == other.amount
        except AttributeError:
            return False
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>

#Exercise 2: Import

#Exercise 3: String Module
import random
import string

def random_string(length = 5):
    letters = string.ascii_lowercase + string.ascii_uppercase  # Generates all lowercase and uppercase letters
    return "".join(random.choice(letters) for i in range(length))

print(random_string())

#Exercise 4: Current Date
import datetime

today_date = datetime.date.today()
print(today_date)

#Exercise 5: Amount of time left until January 1st
import datetime

jan_one = datetime.datetime(2026, 1, 1)
today_date = datetime.datetime.today()
print(jan_one - today_date)

# #Exercise 6: Birthday and minutes
import datetime #always include import datetime

user_bday_string = '1997-04-24'
user_bday_num = datetime.datetime.strptime(user_bday_string, "%Y-%m-%d")
print(user_bday_num)

today = datetime.datetime.now()
user_lived = today - user_bday_num
print(user_lived)

min_alive = user_lived.total_seconds() / 60
print(f'You lived for {min_alive} minutes')

#Exercise 7:Faker Module
from faker import Faker
fake = Faker()
users = []
def add_fake_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

for _ in range(5): 
    add_fake_user()

for user in users:
    print(user)