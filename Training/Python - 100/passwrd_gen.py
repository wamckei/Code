import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '9', '8', '7', '6', '5', '4', '3', '2', '1']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the python password generator!")
pw_letters = int(input("How many letters do you want in your password?\n"))
pw_symbols = int(input("How many special characters do you want in your password?\n"))
pw_numbers = int(input("How many numbers would you like in your password?\n"))

# Easy way - in sequence

password = " "
for i in range(0, pw_letters):
    password += random.choice(letters)

for x in range(0, pw_symbols):
    password += random.choice(symbols)

for y in range(0, pw_numbers):
    password += random.choice(numbers)

# Print PW
print(f"Password is: {password}")



# Harder way - randomize the password

# Empty list defined to hold pw characters
passwrd_lst = []
password1 = " "

# loop through each list to randomly select items based on number of objects desired by end user
for i in range(0, pw_letters):
    passwrd_lst.append(random.choice(letters))

for x in range(0, pw_symbols):
    passwrd_lst.append(random.choice(symbols))

for y in range(0, pw_numbers):
    passwrd_lst.append(random.choice(numbers))

#shuffle content of passowrd to make pw randomized
random.shuffle(passwrd_lst)

# Build password from new list of random objects
for z in passwrd_lst:
    password1 += z

# Print PW
print(f"Password is: {password1}")

