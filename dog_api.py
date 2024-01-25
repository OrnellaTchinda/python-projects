#Download the requests module which is a HTTP library using "pip install requests"
# Import module to Fetch API
import requests

#Ask user to write a breed or give a short selection of breed
#Make everything lower case to control the data and remove the space because the returned data (breed) doesn't have space
user_input = input ("Enter a breed of dog or type breed to get a short list of breeds ").lower().replace(" ", "")

#Selection of breeds
option = ["Bouvier", "Dalmatian", "Husky", "Dingo", "Eskimo"]

while user_input == "breed" :
    user_input = input( "Here is a list to help you ' " + ", ".join(option)+ "' Try again: " )
# if user_input == "breed":
#     print(option)

#Make the request    
dog_data = requests.get(
    f"https://dog.ceo/api/breed/{user_input}/images/random"
)
print(dog_data)
#Return the response in json which is more readable
response = dog_data.json()

#Grab the image link from the json response
image = response["message"]

#Print the link that the user can copy and paste to see the dog

# if image == "Breed not found (master breed does not exist)":
#     user_input = input( "Not a Breed. Here is a list to help you ' " + ", ".join(option)+ "' Try again: " )
    
# else:
print("Copy and Paste this link in your browser : " + image)        

#Optimization: Handling error when file doesn't exist
    
