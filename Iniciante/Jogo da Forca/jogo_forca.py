"""
Author: Samuel Augusto
Date: 22/12/2024
Description: Código que simula um jogo da forca
"""
import random
themes = {
    "Animals":  ['dog','cat','tiger','lion','snake'],
    "Fruits":   ['apple','grape','orange','kiwi','acerola'],
    "Countrys": ['brazil','germany','italy','france','portugal']
}
def display_word():
    return " ".join(hidden_word)
print(f'============================')
print(f'Welcome to the Hangman Game:')
print("Themes:")
for i,j in enumerate(themes.keys(), 1):
    print(f"[{i}] = {j}")
option  = int(input('Enter your option: '))-1
theme_choice = list(themes.keys())[option]
secret_word = random.choice(themes[theme_choice])
print(f'Your theme is {theme_choice}')
attempts = 6
guessed_letters = []
hidden_word = ["_"] * len(secret_word)
while(attempts>0 and "_" in hidden_word):
    print(f'Word: {display_word()}')
    print(f'Attempted letters: {', '.join(guessed_letters) if guessed_letters else 'None'}')
    print(f'Attempts: remaining: {attempts}')
    guess = str(input('Enter a letter: ')).lower()
    if(not guess.isalpha() or len(guess) != 1):
        print('Please... Enter one letter.')
        continue
    if(guess in guessed_letters):
        print('The letter remaining. Try again...')
        continue
    guessed_letters.append(guess)
    if(guess in secret_word):
        print(f'Good! The letter "{guess}" has in word.')
        for index, letter in enumerate(secret_word):
            if(letter==guess):
                hidden_word[index] = guess
    else:
        print(f'The letter "{guess}" has not in word')
        attempts -= 1
if("_" not in hidden_word):
    print(f'\nCongratulations! The word is: {''.join(hidden_word)}\n')
else:
    print(f'\nNot good... the word is: {secret_word}\n')