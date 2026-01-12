# leverage os module to clear screen
import os
from silent_auction_logo import logo

print(logo)
print("Welcome to the silent auction, please enter your bids!")

# Define function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Conditional while variable to terminate loop based on user input
cont_add_bid = True

# Define empty dictionary
user_bid = {}

# Simpler way to do it. 
# while cont_add_bid:
#     user = input("Enter your Name:\n")
#     bid = input("Enter your bid:\n")

#     # Converts string input to interger and removed the dollar sign which is appended back in the print statement for the winner below
#     user_bid[user] = int(bid.replace('$', ''))

#     # Determine if the user wishes to continue to enter in new bids, if no  the winner is selected 
#     restart = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n").lower()
#     if restart == "yes":
#         clear_screen()
#     elif restart == "no":
#         cont_add_bid = False
#         max_key, max_val = max(user_bid.items(), key=lambda x: x[1])
#         print(f"User: {max_key} with auction: ${max_val} Wins!!")


# Alternative route (more logic)

# Define a functiont to calculate highest bidder

def find_highest_bidder(bidding_dictionary):
    # Define a variable to hold the user key of the winner
    winner = ""
    # Define a variable to hold the value for the highest bidder
    highest_bid = 0

    for x in bidding_dictionary:
        bid_amount = bidding_dictionary[x]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = x
    print(f"The Winner is {winner} with a bid of ${highest_bid}")

while cont_add_bid:
    user = input("Enter your Name: ")
    bid = int(input("Enter your bid: $"))

    user_bid[user] = bid

    # Determine if the user wishes to continue to enter in new bids, if no  the winner is selected 
    restart = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n").lower()
    if restart == "yes":
        clear_screen()
    elif restart == "no":
        cont_add_bid = False
        find_highest_bidder(user_bid)
        



