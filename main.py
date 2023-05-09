import random


def check_user_wish():
    if counter == 'y' or counter == 'Y':
        start_game()
    elif counter == 'n' or counter == 'N':
        exit
    else:
        print('Invalid choice.!')
        exit


def start_game():
    player_num = int(input('Guess the number between 1 and 10: '))
    computer_num = random.randint(1, 10)

    if player_num == computer_num:
        print('You guessed it correctly.!')
    else:
        print('You guessed it wrong.!')

    print('Your Guess: ', player_num)
    print('The Number: ', computer_num)


print('<<===========_WELCOME TO THE NUMBER GUESSING GAME_===========>>')
counter = input('Do you want to play the game? (y/n)')
check_user_wish()
