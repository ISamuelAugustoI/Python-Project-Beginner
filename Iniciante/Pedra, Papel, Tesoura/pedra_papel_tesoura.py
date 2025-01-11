"""
Author: Samuel Augusto
Date: 22/12/2024
Description: Código que simula um jogo de pedra papel e tesoura
"""
import random
while True:
    pc_won = 0
    my_won = 0
    print(f'================================================')
    print(f'Welcome to the game of rock, paper, and scissors!')
    print(f'[1] = Rock, [2] = Paper, [3] = Scissors')
    try:
        rounds = int(input('Enter how many rounds: '))
    except ValueError:
        print(f'Invalid input. Please enter a number.')
        continue
    if(rounds<=0):
        print(f'Ok! Come again.')
        break
    options = ["Rock", "Paper", "Scissors"]
    while(rounds>0):
        try:
            my_choice_index = int(input(f'Enter your choice [1-3]: '))-1
            if(my_choice_index not in [0, 1, 2]):
                print("Invalid choice! Choose 1, 2, or 3.")
                continue
            my_choice = options[my_choice_index]
        except(ValueError, IndexError):
            print("Invalid choice! Choose 1, 2, or 3.")
            continue
        pc_choice = random.choice(options)
        print(f'You: {my_choice}, PC: {pc_choice}')
        if(my_choice == pc_choice):
            print(f"It's a Tie!")
        elif(my_choice=="Rock"     and pc_choice=="Scissors") or \
            (my_choice=="Paper"    and pc_choice=="Rock") or \
            (my_choice=="Scissors" and pc_choice=="Paper"):
            print(f'You Won!!!')
            my_won+=1
        else:
            print(f'You Lost...')
            pc_won+=1
        rounds-=1
        print(f'Remaining rounds: {rounds}')
    print('================================================')
    if(my_won == pc_won):
        print(f"Tie... Good game. Final score: You {my_won} - {pc_won} PC")
    elif(my_won > pc_won):
        print(f"Nice! You won!!! Final score: You {my_won} - {pc_won} PC")
    else:
        print(f"You lost... Pathetic. Final score: You {my_won} - {pc_won} PC")
    print('================================================')