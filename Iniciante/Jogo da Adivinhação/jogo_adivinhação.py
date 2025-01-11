"""
Author: Samuel Augusto
Date: 22/12/2024
Description: Jogo que simula um jogo de adivinhação de números
"""
import random
guess = 0
while True:
    print(f'=============================')
    print(f'Welcome to the Guessing Game!')
    chosen_number = random.randint(1,10)
    while True:
        choice_number = int(input('Enter the choice number[1-10]: '))
        guess+=1
        if(choice_number==chosen_number):
            print(f'Nice! You got it right!!! [{chosen_number}]')
            print(f'you had {guess} guesses')
            break
        else:
            print(f'No... Try again.')
            print(f'--------------------')
            if(choice_number>chosen_number):
                print(f'The number is lower')
            else:
                print(f'The number is bigger')
            print(f'--------------------')