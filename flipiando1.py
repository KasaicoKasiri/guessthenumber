import random
from random import shuffle
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

random.shuffle(numbers)
just_one = []
just_one.append(numbers[4])
print('########################################################################')
print('############# Welcome to play Guess what is the number #################')
print('########################################################################\n')

player_game = input("Welcome Player what is your name? ")
respond = input(f' Welcome {player_game} are you ready to try your luck? y/n?')
if respond == "y":
    guess_who = "wrong"

    while True:
        guess_who = int(input("Guess what is the number 1 from 20 : "))

        if guess_who == numbers[4]:



            print(f"You won {player_game} thanks for play")
            break


        else:

            print(f'{player_game} you lose')

            try_again = input(f'{player_game} are you ready to try again? y/n?')

            if try_again == 'y':

                guess_whos = guess_who

            else:
                print(f'{player_game} I hope you back later, thanks')
                break




else:
    print(f'{player_game} I hope one day you come and try your luck')