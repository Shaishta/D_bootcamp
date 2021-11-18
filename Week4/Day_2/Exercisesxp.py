# Exercises XP

# Exercise 1 : Favorite Numbers
# my_fav_numbers = {5, 7, 10, 12, 25}
#
# my_fav_numbers.add(11)
# my_fav_numbers.add(24)
#
# remove = my_fav_numbers.pop()
#
# print(remove)
# print(my_fav_numbers)
#
# friend_fav_numbers = {26, 34, 17, 89}
# print(friend_fav_numbers)
#
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#Exercise 2: Tuple
#no they are immutable.

#Exercise 3: Print A Range Of Numbers
# for i in range (1,13):
#     print(i)

#Exercise 4: Floats
#float() is when a value is converted to a point number
# as a list

# a_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# print(a_list)

#Exercise 5: Shopping List
#basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0,'Apples')
# basket.count("Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

#Exercise 6 : Loop
# name = ''
# while name != 'Shaishta':
#   name = input('What is your name? ')
#
# print('You entered the right name!')

#Exercise 7
# basket = ["Banana", "Apples", "Oranges", "Blueberries", "Kiwi", "Mango", "Pineapple"]
# count = 0
# for even in basket:
#
#     if count % 2 == 0:
#         print(even)
#
#    count += 1

#Exercise 8
# divisible = []
# for x in range(1500, 2500):
#     if (x % 7 == 0) and (x % 5 == 0):
#         divisible.append(str(x))
# print(','.join(divisible))

#Exercise 9: Favorite Fruits
# fav_fruit = input("Enter your favourite fruit(s),(please add a single space to separate the fruits): ")
# fav_fruit.split()
# print(fav_fruit.split())
#
# new_fruit = input("Enter the name of any fruit: ")
# if new_fruit in fav_fruit:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

#Exercise 10: Who Ordered A Pizza ?
# active = True
#
# while active:
#     topping = input("Please enter your pizza toppings (enter 'quit' when you are finished): ")
#     if topping == 'quit':
#         active = False
#     else:
#         print("Pizza topping: ", topping)
#
# print("The total price is 10 + 2.5 for each topping.")

#Exercise 11: Cinemax

#     name = input("Please enter your name: ")
#     age = int(input("Please enter your age: "))
#
#     if age < 3:
#         print("The ticket is free.")
#     elif age in range(3, 12):
#         print("Ticket is $10.")
#     elif age > 12:
#         print("Ticket is $15.")
#
#     elif age in range(16, 21):
#         print("not permitted to watch movie")
#     else:
#         print("permitted to watch movie")
# print(name.split(), age)

#Exercise 12 : Who Is Under 16
# name_list = ['Lily', 'John', 'Anna', 'Park']
#
# name = input("Enter your name: ")
# if name in name_list:
#     age = int(input("Enter your age: "))
# if age < 16:
#     name_list.remove(name)
#
# print(name_list)

# #Exercise 13
# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []
#
# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# print("\n")
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)
#
# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")



