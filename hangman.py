#import random
import random

#Get a list of words
options = ["carotte", "poivron", "poireau" ]

#The computer randomnly choose among a list of words
computer = random.choice(options)
# Change it to an array to be able to pinpoint each letter and index
computer_list = list(computer)
print(computer_list)
#Print it's a vegetable
print("Hint! It's a one word vegetable")

#return a list of underscore with the number of letters of the guessing game
x="_"
guessed_words = x * len(computer_list)
print (guessed_words)
guessed_words_list =[]
#Ask the user to input a letter
user_input = input("Choose a letter : ")

#number of chances is length of the word plus 2
chances = len(computer_list) + 2
#while the number of chances is more than 0
while chances > 0:
    
#Should only be one letter
    if len(user_input) >1:
        print("Only one letter please, try again")
        chances -=1 
        continue    
#if letter already entered
    elif user_input in guessed_words_list :
        print("Already guessed this letter")
        
#If letter is in the list, go the list of underscore and change the index of the underscore which is the same index of the list of the word and chances' number goes down by one
    elif user_input in computer_list:
        for user_input in guessed_words_list: 
                if user_input in guessed_words_list: 
                    print(user_input, end=' ') 
                    chances += 1
                    # If user has guessed all the letters 
                    # Once the correct word is guessed fully, 
                elif (count(guessed_words_list) == count(computer_list)):
        # number_of_occurences = computer_list.count(user_input)
        # guessed_words[]
        # chances -=1 
        # continue
        
#If letter is not in the list; counter down to 0 and ask the user to try again
    else:
        print("Letter not in the word")
        chances -=1 
    break
        
if chances == 0 & count():
    print("The word is "+ computer)