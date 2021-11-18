#Exercises XP Gold
#Exercise 1: Birthday Look-Up
# from datetime import datetime
#
# birthdays = {"Anna": "2001/7/22",
#              "Sam": "2000/12/5",
#              "John": "1999/5/20",
#              "Joy": "2000/10/1",
#              "Mary": "1998/2/24"}
# print("Hello!! You can look up the birthdays of the people in the list!")
# name = input("Please enter a name: ")
# # for i in birthdays:
# if name in birthdays:
#     print(name, "is born on", birthdays[name])
# else:
#     print("hi")

#Exercise 2: Birthdays Advanced
# from datetime import datetime
#
# birthdays = {"Anna": "2001/7/22",
#              "Sam": "2000/12/5",
#              "John": "1999/5/20",
#              "Joy": "2000/10/1",
#              "Mary": "1998/2/24"}
# print("Hello!! You can look up the birthdays of the people in the list!")
# print(birthdays)
# name = input("Please enter a name: ")
# # for i in birthdays:
# if name in birthdays:
#     print(name, "is born on", birthdays[name])
# else:
#     print("Sorry, we don’t have the birthday information for", name)
#
# #Exercise 3: Add Your Own Birthday
# from datetime import datetime
# datetime.strptime("2001/07/22","%Y/%m/%d")
#
# birthdays = {"Anna": "2001/07/22",
#              "Sam": "2000/12/05",
#              "John": "1999/05/20",
#              "Joy": "2000/10/01",
#              "Mary": "1998/02/24"}
# print("Hello!! You can look up the birthdays of the people in the list!")
# print(birthdays)
# new_name = input("Please enter your name: ")
# dob = input("Please enter your birthdate(in 'yyyy/mm/dd format): ")
# birthdays.update({new_name: dob})
# for k, v  in birthdays.items():
#     birthdays[k] = datetime.strptime(v, "%Y/%m/%d")
# print(birthdays)
# print(birthdays["Anna"].year)
#
# name = input("Please enter a name: ")
# # for i in birthdays:
# if name in birthdays:
#     print(name, "is born on", birthdays[name])
# else:
#     print("Sorry, we don’t have the birthday information for", name)

#Exercise 4: Fruit Shop
# items={
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# for i in items:
#     print("A", i, "is", items[i])
#     item = {i: items[i]}
#     print(item)
# total_price= []
# total_price = sum(list(items.values()))
# print(total_price)

#
# #Exercise 5 : Cars
# str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
# list1 = str.split()
# print(list1)
# print('there are', ''.join(list1))
# list1.reverse()
# print(list1)
# result_dict = {}
#
# for k, v in zip(list1, list(range(len(list1)))):
#     if 'o' in k:
#         result_dict[k] = v
# print(result_dict)
