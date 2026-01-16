import random
import os
from num_guess_app_logo import logo

print(logo)

attempts = 0
end_of_game = False
no_match = True
computer_num = random.randint(1, 100)
print("Welcome to the Number Game!")
print("I am thinking of a number between 1 and 100.")
answer_level = input("Choose a difficulty. Type 'easy' or 'hard':  ")

def compare(x1, y1,):
    """Compare the computers random number to the user guess"""
    if x1 > y1:
        return"Too High! Guess Again"

    elif x1 < y1:
        return "Too Low! Guess again"
    else:
        return "correct"
        

def game_attempt(turn):
    turn -= 1

while not end_of_game:
    
    if answer_level == "easy":
        attempts = 10
    elif answer_level == "hard":
        attempts = 5

    while no_match:

        if attempts == 0:
            print("You are out of attempts, game over!")
            end_of_game = True
            break

        user_select = int(input("Make a guess:  "))
        
        if compare(user_select, computer_num) == "correct":
            print(f"You guessed correctly!! The number was: {computer_num}")
            end_of_game = True
            no_match = False
        elif attempts == 0:
            print("You are out of attempts, game over!")
            no_match = False
            end_of_game = True
        else:
            print(compare(user_select, computer_num))
            attempts = attempts -1
            print(f"You have: {attempts} left")
        








