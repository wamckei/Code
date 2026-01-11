print("Welcome to the rollercoaster!")

height = int(input("How tall are you in cm? "))
ticket_cost = 0

if height > 80:
    print("Tall enough to ride ")
    age = int(input("How old are you? "))
    if age <= 12:
        print(" Your ticket cost $5")
        ticket_cost = 5
    elif age <= 18:
        print(" Your ticket cost $7")
        ticket_cost = 7
    elif 45 <= age <= 55:       #simplar way (less interpretable) than "age >=45 and age <= 55"  
        print("Your ticket is free! ")      
    else:
        print("Your ticket cost $12")
        ticket_cost = 12

    picture = input("Do you want too have a photo taken? Enter y for yes and n for no: ")
    if picture == "y":
        ticket_cost += 3 
        print(f"Your final bill is {ticket_cost}")
    else:
        print(f"Your final bill is {ticket_cost}")
else:
    print("to short to ride the rollercoaster, sorry!")