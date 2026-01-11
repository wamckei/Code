import random

# ASCII Art for images

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors =  """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Code
# Input for choice from user: rock, paper, or scissors
choice = int(input("Please choose one of the following: 1 for Rock, 2 for Paper, or 3 for Scissors: "))
#computer pics at random between the 3
comp_choice = random.randint(1, 3)

# Conditional statement to print out the ASCII value from the user choice
print(f"You choice: {choice}")
if choice == 1:
    print(rock)
elif choice == 2:
    print(paper)
else:
    print(scissors)

# Condisional statement to print out the ASCII value of the computers choice
print(f"Computers choice: {comp_choice}")
if comp_choice == 1:
    print(rock)
elif comp_choice == 2:
    print(paper)
else:
    print(scissors)

# Conditional statement for rock, paper, scissors rules, evaluates the conditions to see who wins. 
if choice == 1 and comp_choice == 2:
    print("You Lose!! ")
elif choice == 2 and comp_choice == 1:
    print("You WIN!!")
elif choice == 2 and comp_choice == 3:
    print("You Lose!! ")
elif choice == 3 and comp_choice == 2:
    print("You WIN!!") 
elif choice == 3 and comp_choice == 1:
    print("You Lose!! ")
elif choice == 1 and comp_choice == 3:
    print("You WIN!!") 
elif choice == comp_choice:
    print("Its a Tie !!!!")
else:
    print("Incorrect Value entered, boo. ")