#Daily Challenge: OOP Quizz

#Part 1 : Quizz :

"""
1. What is a class?
Answer :
A class is used to create object that is, it is an object constructor.

2. What is an instance?
Answer:
An instance is an object created from a class.

3. What is encapsulation?
Answer:
Encapsulation is used to restrict access to methods and variables and can prevent data from being modified.

4. What is abstraction?
Answer:
Abstraction is used to hide the irrelevant data/class in order to reduce the complexity.

5. What is inheritance?
Answer:
Inheritance is a way by which a subclass can inherit the attributes and methods of another class.

6. What is multiple inheritance?
Answer:
Multiple Inheritance is a type of inheritance in which one class can inherit properties (attributes and methods) of more than one parent classes.

7. What is polymorphism?
Answer:
polymorphism means different or related classes that use the same names for their functions and allows the ability to use a standard interface for multiple forms or data types.

8. What is method resolution order or MRO?
Answer:
MRO defines the order in which the base classes are searched when executing a method.

"""

#Part 2: Create A Deck Of Cards Class

import random

suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for value in value_list for suit in suit_list]

    def shuffle(self):
        random.shuffle(self.cards)
        for card in self.cards:
            print(card.suit, card.value)
        return self.cards

    def deal(self):
        x = random.choice(self.cards)
        print(x.suit, x.value)
        self.cards.remove(x)
        for card in self.cards:
            print(card.suit, card.value)


a = Deck()
a.shuffle()
a.deal()

