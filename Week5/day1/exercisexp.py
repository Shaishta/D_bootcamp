# Exercises XP
# Exercise 1: Cats

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.cat_name = cat_name
#         self.cat_age = cat_age
#
# cat1 = Cat('Lucy',3)
# cat2 = Cat('Milo',2)
# cat3 = Cat('Lily',5)
#
# def oldest(list_of_cats):
#     list_of_ages = []
#
#     for cat in list_of_cats:
#         list_of_ages.append(cat.cat_age)
#     return max(list_of_ages), list_of_cats[list_of_ages.index(max(list_of_ages))].cat_name
# list_of_cats = [cat1, cat2, cat3]
#
# print(f'The oldest cat is {oldest(list_of_cats)[1]} and is {oldest(list_of_cats)[0]} years old.')

# #Exercise 2 : Dogs
#
# class Dog():
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#
#     def bark(self):
#         print(f"{self.name} goes woof!")
#
#     def jump(self):
#         print(f"{self.name} jumps {self.height*2} cm high!")
#
# doggy = Dog("Bob", 40)
# doggy.bark()
# doggy.jump()
#
# davids_dog = Dog("Rex", 50)
# davids_dog.bark()
# davids_dog.jump()
#
# sarahs_dog = Dog("Teacup", 20)
# sarahs_dog.bark()
# sarahs_dog.jump()
#
# bigger_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name
# print(bigger_dog)


#Exercise 3 : Who’s The Song Producer?
# class Song():
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
# stairway= Song(["There’s a lady who's sure",
#                 "all that glitters is gold",
#                 "and she’s buying a stairway to heaven"])
#
# print(stairway.sing_me_a_song())

# #Exercise 4 : Afternoon At The Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.pens = {}
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            pass
    def get_animals(self):
        print(",".join(self.animals))
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            print(f"Goodbye {animal_sold} !")
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo.")
    def sort_animal(self):
        copy = self.animals.copy()
        copy.sort()
        list_of_lists = []
        temp = []
        temp.append(copy.pop(0))
        while len(copy) > 0:
            if temp[0][0] == copy[0][0]:
                temp.append(copy.pop(0))
            else:
                list_of_lists.append(temp)
                temp = []
                temp.append(copy.pop(0))
        list_of_lists.append(temp)
        num_list = [i for i in range(len(list_of_lists))]
        result_dict = {key: value for key, value in zip(num_list, list_of_lists)}
        self.pens = result_dict
    def get_pens(self):
        for pen in self.pens.items():
            print(f"in pen {pen[0]} there are: {','.join(pen[1])}")

zoo = Zoo('Casela nature park')
zoo.add_animal('Lion')
zoo.add_animal('Giraffe')
zoo.add_animal('Leopard')
zoo.add_animal('Bear')
zoo.add_animal('Bat')
zoo.get_animals()
zoo.sell_animal('Lizard')
zoo.sell_animal('Lion')
zoo.get_animals()
zoo.add_animal('Lion')
# sorted_animals = zoo.sort_animal()
zoo.sort_animal()
zoo.get_pens()
