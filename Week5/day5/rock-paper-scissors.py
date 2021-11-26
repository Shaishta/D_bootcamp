from game import Game


def print_results(results):
    print(results)


def get_user_menu_choice():
    menu = input(" Menu:Play a new game: (a), Display scores: (d), Quit: (q) ")
    return menu


def main():
    li = []
    while True:
        x = get_user_menu_choice()
        if x == "a" or x == "d" or x == "q":
            if x == "a":
                a = Game()
                y = a.play()
                li.append(y)
            elif x == "d":
                print_results({"win": li.count("win"), "loss": li.count("loss"), "draw": li.count("draw")})
            else:
                print_results(f""" Game results:
                You won {li.count("win")} times
                You lost {li.count("loss")} times
                You drew {li.count("draw")} times.
                Thank you for playing!!
                """)
                break

        else:
            print("Not a valid input!")


main()
