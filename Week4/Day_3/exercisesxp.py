#Exercises XP
#Exercise 1 : Convert Lists Into Dictionaries
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# key_dictionary = dict(zip(keys, values))
# print(key_dictionary)

#Exercise 2 : Cinemax #2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# age = int(input("Enter age or enter '0' to quit:"))
# price = []
# active = True
# while age != 0:
#     age = int(input("Enter age or enter '0' to quit:"))
#     # for i in list:
#     if age <= 3:
#         price.append(0)
#     elif age > 3 and age < 12:
#         price.append(10)
#     elif age == 0:
#         active = False
#     else:
#         price.append(15)
# print(price)
# family_prices = zip(family.keys(), price)
# prices = {}
# for i, j in family_prices:
#     prices[i] = j
# print(family_prices)
# print(prices)

#Exercise 3: Zara
# brand = {"name": "Zara",
#          "creation_date": 1975,
#          "creator_name": "Amancio Ortega Gaona",
#          "type_of_clothes": "men, women, children, home",
#          "international_competitors": ["Gap", "H&M", "Benetton"],
#          "number_stores": 7000,
#          "major_color": {"France": "blue", "Spain": "red", "US": "pink, green"}}
#
# brand['number_stores'] = 2
# print(brand['number_stores'])
# print("The clients of", brand['name'], "are", brand['type_of_clothes'])
# brand['country_creation'] = "Spain"
# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')
# del brand['creation_date']
# print(brand)
# print(brand['international_competitors'][-1])
# print(brand['major_color']['US'])
# print("len() method :", len(brand))
# for key in brand.keys():
#     print("The keys are:", key)
#
# more_on_zara = {"creation_date": 1975,
#                 "number_stores": 10000}
# brand.update(more_on_zara)
# print(brand)
# print(brand['number_stores'])#the number of stores got override

#ex4
# # 1/
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# result_dict = {}
#
# for k, v in zip(users, list(range(len(users)))):
#     if 'i' in k and k[0] in ['M', 'P']:
#         result_dict[k] = v
# #2/
# for k, v in zip(list(range(len(users))), users):
#     result_dict[k] = v
#
# #3/
# for k, v in zip(sorted(users), list(range(len(users)))):
#     result_dict[k] = v


