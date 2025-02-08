#Write a function called save_json. This function takes a dictionary below as an argument 
# and saves it on a file in JSON format.
#names = {'name': 'Carol','sex': 'female','age': 55
names = {'name': 'Carol','sex': 'female','age': 55}
import json
def save_json(names):
    with open('names.json', 'w') as file:
        json.dump(names, file)
save_json(names)
print(names)







#Write another function called read_json that opens the file that you just saved and reads its content.