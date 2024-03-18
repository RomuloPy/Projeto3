from random import randint
from time import sleep


def pause():
    input('Press ENTER to continue...')


def exit_game():
    exit_message = ('The program will exit in a few seconds...')
    print('*' * len(exit_message))
    print(exit_message)
    print('*' * len(exit_message))
    sleep(3)
    print('')
    sleep(1)
    print('###  Have a nice day!  ###')
    

pause()
while True:
    random_number = randint(1, 100)
    print('A number between 1 and 100 has been generated...')
    my_guess = int(input('Try to guess that number: '))
    while my_guess != random_number:
        if my_guess > random_number:
            my_guess = int(input('You need to go LOWER...'))
        elif my_guess < random_number:
            my_guess = int(input('You need to go HIGHER...'))
    print(f'Congratulations! You just guess the generated number!({random_number})')
    play_again = input('Would you like to play again? [S/N]: ')
    if play_again.upper() == 'N':
        exit_game()
        break
