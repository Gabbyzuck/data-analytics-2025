# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# A Class is a set of behaviors that defines objects with attributes.

# What is an instance?
# An Instance is an outcome defined by the class's parameters.

# What is encapsulation?
# Encapsulation is the privitazation of certain attributes or methods.

# What is abstraction?
# Abstraction is utilizing just the main functions of an objects.

# What is inheritance?
#Inheritance is when a child class absorbs the attributes of a parent class to act in the same way in order to carry out the same behaviors in a new class.

# What is multiple inheritance?
# Multiple inheritance is when a child class inherits attributes and methods from more than one parent class.

# What is polymorphism?
# Polymorphism is treating objects of different classes as objects in one superclass.

# What is method resolution order or MRO?
#MRO is the order in which Python looks for the method to execute when inheriting a class. 

# Part 2: Create a deck of cards class.
import random 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"  # String representation of the card

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        self.cards = [Card(suit, value) for suit in suits for value in values]  # lists all 52 cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self): 
        if len(self.cards) == 0:
            return "No cards left in deck." #message once deck is empty
        return self.cards.pop() #deletes and return last card

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards: {', '.join(map(str, self.cards))}"  # Return a string representation of the deck

a_spade = Card('Spade','A')
print(a_spade.__repr__())

deck = Deck()
print(deck)

deck.shuffle()
print(deck)

print(deck.deal())
print(len(deck.cards))
