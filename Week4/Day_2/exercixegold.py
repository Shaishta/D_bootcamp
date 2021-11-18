#Exercises XP Gold
#Exercise 1 : Concatenate Lists

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# for i in list2 :
#     list1.append(i)
# print(list1)

#Exercise 2: Greatest Number
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# if (num1 > num2) and (num1 > num3):
#     largest = num1
# elif (num2 > num1) and (num2 > num3):
#     largest = num2
# else:
#     largest = num3
#
# print("The largest number is", largest)

#Exercise 3 : The Alphabet
# str = 'abcdefghijklmnopqrstuvwxyz'
# print(str)
#
# alpha = input("Insert a letter of the alphabet: ")
# if alpha in ("a", "e", "i", "o", "u"):
#     print(alpha + " is a vowel.")
# else:
#     print(alpha + " is a consonant.")

#Exercise 4
#
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#
# item = input("Enter your name: ")
#
# index = names.index(item)
#
# print('the index of', item, 'in the list is:', index)

#Exercise 5 : Words And Letters
# words = input("insert 7 words please: ")
# list1 = list(words)
# letter = input("insert a single character: ")
#
# index = words.index(letter)
# print('the index of', letter, 'in the word', words, 'in the list is:', index)
#
# if letter not in words:
#     print('Sorry!', letter, 'is not in the word!')
# Exercise 6
# numbers = list(range(1, 1_000_001))
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

#Exercise 7
# numbers = input("Type in numbers separated only by a comma :")
# numbers_split = numbers.split(',')
#
# number_tuple = tuple(numbers_split)
#
# print(numbers_split)
# print(number_tuple)

#Exercise 8 : Random Number
# import random
# random_number = random.randint(1, 10)
# tries = 1
#
# num = int(input("input a number from 1 to 9: "))
#
# if num > random_number:
#     print("Guess Lower...")
# if num < random_number:
#     print("Guess Higher...")
#
# while num != random_number:
#     tries += 1
#     num = int(input("Try Again : "))
#     if num < random_number:
#         print("Guess Higher...")
# if num == random_number:
#     print("You're Right! you win! The Number Was", random_number, "and it only", tries, "tries!")
#

