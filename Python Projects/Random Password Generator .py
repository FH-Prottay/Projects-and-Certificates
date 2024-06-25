#This project creates a random password and the user decides the number of characters
import random

letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=['0','1','2','3','4','5','6','7','8','9','0']
symbol= ['#' ,'$', '%' ,'&' ,'~', '_', '^', '!', '{' ,'}' ,'%', '(', '*', ')' ,'-', '[', '|' ,']' ]
password = []  #this list will store the password

#Taking inputs and converting into integers
n_letter=int(input("How many letters do you want? "))
n_number=int(input("How many numbers do you want? "))
n_symbol=int(input("How many symbols do you want? "))

#we will use loop to store the exact amount of characters that the user inputs
for i in range(1, n_letter+1):
    char= [random.choice(letter)]
    password= char + password

for i in range(1, n_number+1):
    char= [random.choice(number)]
    password= char + password

for i in range(1, n_symbol+1):
    char= [random.choice(symbol)]
    password= char + password

# now we have to shuffle the list
random.shuffle(password)

#Creating an empty string and changing the list to string
Password = ""
for j in password:
    Password= Password+j
print(f"The password is {Password}",)
