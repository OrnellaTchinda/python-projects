import random
from hangman_stick import get_hangman



mylist = ["tiger", 'lion', 'king','toggog']
guess_available = 6
guessed_letters = []
word = random.choice(mylist).lower()


print(word)
print("welcome to the Hangman Game")
print(get_hangman(guess_available))


for char in word:
    print(" _ ",end="")
print()



def take_input():
    flag = True
    global guessed_letters
    print("Please guess the letter: ")
    while flag: 
        guess = input().lower()
        if len(guess) != 1: 
            print("\nPlease enter a single letter: ")
        elif not guess.isalpha(): 
            print("\nPlease enter alphabet letter (a-z): ") 
        elif guess in guessed_letters:  
            print("You already enter that letter, please enter another letter") 
        else: 
            #print("testing")
            flag = False
    return guess   




while ((guess_available > 0) & (len(guessed_letters) < len(word))) :


    print("\nguess available: {}\n".format(guess_available))
    guess = take_input()
    
    if (guess in word) & (guess not in guessed_letters):
        print("\nCorrect guess \n")
        number_of_occurences = word.count(guess)
        #For every occurence of the letter inside the word, add it inside the guessed_letters list
        for _ in range(number_of_occurences):
            guessed_letters+=guess
    else: 
        print('\nIncorrect guess \n')
        guess_available -= 1
        
    print(get_hangman(guess_available))


    for letter in word: 
        if letter in guessed_letters: 
            print(" \x1B[4m " + letter + " \x1B[0m ", end = "")
        else: 
            print("  _  ",end="")
    print()
print()


if guess_available <= 0: 
    print("You Lost")
    print(guessed_letters)
else:
    print("You WIn")
    print(guessed_letters)