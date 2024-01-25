import random
# print("Ornella est fun")

# children = {
#     "Mike":"one",
#     "Kimbo": "deux"
# }

# print (children)

# for key in children:
#     print(key, children[key])
    
# for key,value in children.items():
#     print(key, value)

# name = input("your name?")

# num1 = input("Enter a number")
# operator = input("Enter operator")
# num2 = input("Enter a number")


# if operator == "+" :
#     result = float(num1) + float(num2)
# elif operator == "-":
#     result = float(num1) - float(num2)
# elif operator == "*":
#     result = float(num1) * float(num2)
# elif operator == "/":
#     result = float(num1) / float(num2)
    
# print(result)

#Rock Paper Scissors


user_input = input("Type Rock Paper or Scissors: ").lower().replace(" ", "")

values_rps = ["rock", "paper", "scissors"]
    
while user_input not in values_rps :
    user_input = input("Try again: ")
         
computer_choice = random.choice(values_rps)

print("Computer chose", computer_choice)

if user_input == computer_choice:
    print("Tie")    
elif user_input == "rock" and computer_choice == "scissors":
    print("You won!!!")
elif user_input == "paper" and computer_choice == "rock":
    print("You won!!!")
elif user_input == "scissors" and computer_choice == "paper":
    print("You won!!!")
else:
    print("Computer won")
        
    


