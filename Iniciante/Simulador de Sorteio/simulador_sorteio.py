"""
Author: Samuel Augusto
Date: 22/12/2024
Description: Código sobre um simulador de sorteio de nomes
"""
import pygame
import random
import os
os.chdir("C:/Users/Samsung/Downloads/Programação/[Portfolio]/Python/Iniciante/Simulador de Sorteio/")
while True:
    array = []
    print(f'\n==================================')
    print(f'Welcome to Samuel\'s Draw Simulator')
    participants = int(input(f'Enter how many peoples will participate: '))
    if(participants<=0):
        break
    for i in range(1,participants+1):
        participant = str(input(f'Enter the {i}º name: '))
        array.append(participant)
    drawn = int(input(f'Enter how many peoples will be drawn: '))
    chosen = random.sample(array,drawn)
    print(f'\nParticipants:')
    for i in array:
        print(i)
    print(f'\nRaffleds:')
    cont = 1
    pygame.mixer.init()
    pygame.mixer.music.load("./success.mp3")
    pygame.mixer.music.play()
    for i in chosen:
        print(f'{cont}º = {i}')
        cont+=1
    repeat = str(input("\nDo you want to make another draw? (y/n): ")).strip().lower()
    if(repeat != 'y'):
        print("Ending the simulator...")
        break