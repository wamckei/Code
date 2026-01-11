print("Welcome To Python Pizza Deliveries!")
size = input("What pizza size would you like? S, M or L: ")
pepp = input("Do you want pepperoni on your pizza? y or n :")
extra_cheese = input("Do you want extra cheese? y or n: ")
pizza_bill = 0

if size.upper() == "S":
    pizza_bill += 8
elif size.upper() == "M":
    pizza_bill += 12
elif size.upper() == "L":
    pizza_bill += 15
else:
    print("Incorrect input, please try again")

if pepp.upper() == "Y":
    if size.upper() == "S":
        pizza_bill += 2
    else:
        pizza_bill += 3

if extra_cheese.upper() == "Y":
    pizza_bill += 1

print(f"You total bill is ${pizza_bill}")



