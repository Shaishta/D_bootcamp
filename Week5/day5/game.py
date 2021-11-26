import random

class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        while True:
            item = input("Please choose between Rock(r), Paper(p), Scissors(s): ")
            if item == "r" or item == "p" or item == "s":
                return item
            else:
                print("Not a valid input!")

    def get_computer_item(self):
        comp_choice = random.choice(["r", "p", "s"])
        return comp_choice

    def get_game_result(self, user_item, computer_item) :
# results: draw, win, lose,(rock beating scissors, paper beating rock, and scissors beating paper)
        if user_item == computer_item:
            return "draw"

        elif user_item == "r" and computer_item == "s":
            print("Rock wins!!!! The Computer Loses.")
            return "win"

        elif user_item == "s" and computer_item == "p":
            print("Scissors won!!!! The Computer loses.")
            return "win"

        elif user_item == "p" and computer_item == "r":
            print("Paper won!!!! The Computer loses.")
            return "win"

        elif user_item == "r" and computer_item == "p":
            print("The Computer won!!!!  Rock loses.")
            return "loss"

        elif user_item == "s" and computer_item == "r":
            print("The Computer won!!!! Rock loses.")
            return "loss"

        elif user_item == "p" and computer_item == "s":
            print("The Computer won!!!! Paper loses.")
            return "loss"

    def play(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        result = self.get_game_result(self.user_item, self.computer_item)
        print(f'you chose : {self.user_item}, computer : {self.computer_item}, result : {result}')
        return result