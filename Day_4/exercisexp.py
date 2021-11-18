#Exercises XP #1
#Exercise 1 : What Are You Learning ?
# def display_message():
#     msg = "I'm learning to store code in functions."
#     print(msg)
# display_message()

#Exercise 2: What’s Your Favorite Book ?
# def favorite_book(title):
#
#     print(f"One of my favorite books is {title}.")
#
# favorite_book('The Alchemist')

#Exercise 3 : Some Geography
# def describe_city(city, country='Mauritius'):
#     msg = f"{city.title()} is in {country.title()}."
#     print(msg)
#
# describe_city('port-louis')
# describe_city('tel aviv', 'israel')
# describe_city('curepipe')

#Exercise 4 : Random
# import random
#
# number = random.randint(1, 100)
#
# guess = input("Please enter a number: ")
# def num():
#
#     if guess == number:
#         print('Good job! You guessed it right!')
#
# if guess != number:
#     number = str(number)
#     print('Nope. The number I was thinking of was ' + number)
# num()

#Exercise 5 : Let’s Create Some Personalized Shirts !
# def make_shirt(size='large', message="Hi!Python"):
#
#     print(f"\nI'm going to make a {size} t-shirt.")
#     print(f'It will say, "{message}"')
#
# make_shirt()
# make_shirt('medium', "Hello Python")

#Exercise 6 : Magicians …
# magicians = ["Penn and Teller", "David Copperfield", "Jeff McBride"]
# def show_magicians():
#     for name in magicians:
#         print(name)
#
# def make_great():
#     for i in range(len(magicians)):
#         magicians[i] = 'The Great ' + magicians[i] + ' !'
# make_great()
# show_magicians()