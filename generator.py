import string
from random import shuffle
from pyfiglet import figlet_format
from termcolor import colored


print(colored(figlet_format("Yousif"),color="blue"))


upperCase = list(string.ascii_uppercase)
lowerCase = list(string.ascii_lowercase)
Digits = list(string.digits)
Punc = list(string.punctuation)

characters_number = input("How Many Characters Do You Want? ")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6 :
            print("You Need At Least 6 Characters")
            characters_number = input("please enter the number again: ")
        else:
            break
    except:
        print("Please Enter Numbers Only")
        characters_number = input("How Many Characters Do You Want? ")


shuffle(upperCase)
shuffle(lowerCase)
shuffle(Digits)
shuffle(Punc)

part1 = round(characters_number * (30/100) )
part2 = round(characters_number * (10/100) )

password = []

for i in range(part1):
    password.append(upperCase[i])
    password.append(lowerCase[i])
    password.append(Digits[i])

for n in range(part2):
    password.append(Punc[n])    


shuffle(password)

password = "".join(password)
print(password)
