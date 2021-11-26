from anagram_checker import AnagramChecker

def menu():
    a = AnagramChecker()
    while True:
        user_choice = input('''Please enter 'a' or 'b':
        (a): play
        (b): exit
        : ''')

        if user_choice == 'b':
            print('You have decided to exit!')
            break
        elif user_choice == 'a':
            while True:
                user_word = input('Please enter a  word: ')
                if len(user_word.split()) > 1:
                    print('Please enter one word')
                else:
                    if a.is_valid_word(user_word):
                        if user_word.isalpha():
                            user_word.strip()
                            print(f'your word: {user_word.upper()}')
                            return f' anagrams for your word: {",".join(a.get_anagrams(user_word))}.'
                        else:
                            print('Not a valid input!')
                    else:
                        print('Not a valid word!')
        else:
            print("Please enter with 'a' or 'b' only!")
print(menu())