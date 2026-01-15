import random
import os
from blackjack_app_logo import logo

print(logo)

#TODO: 

# Rules: 
# The deck is unlimited in size
# There are no Jokers
# The Jack, King, & Queen = 10
# The Ace can count as 1 or 2
# The cards in the list have equal probability of being drawn
# Cards are not removed from the deck when they are drawn
# The computer is the dealer



# Define Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck"""
    # List of card values - Ace is represented by 11 unless 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
def calculate_score(cards):
    """Calculates scores for the user and dealer then returns the sum if not 21, if 21 it returns 0"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(u_score, d_score):
    if u_score == d_score:
        return "Draw"
    elif d_score == 0:
        return "You Lose, dealer has blackjack!"
    elif u_score == 0:
        return "Congratuations, you Win with a blackjack!!!!"
    elif u_score > 21:
        return "You busted, went over 21. You Lose!!"
    elif d_score > 21:
        return "You Win!! Dealer busted and went over 21!!"
    elif u_score > d_score:
        return "You Win"
    else:
        return "You Lose"
def play_game():

    user_card = []
    dealer_card = []
    dealer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())


    while not is_game_over:

        user_score = calculate_score(user_card)
        dealer_score = calculate_score(dealer_card)
        print(f"your cards {user_card}, current score:{user_score}")
        print(f"Dealer card: {dealer_card[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            answer = input("Do you wish to hit? 'y' for Yes and 'n' for No:  ").lower()
            if answer == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_card.append(deal_card())
        dealer_score = calculate_score(dealer_card)

    print(f"Your final hand was: {user_card}, final score was: {user_score}")
    print(f"Dealer final hand was: {dealer_card}, dealer final score was: {dealer_score}")
    print(compare_score(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower() == "y":
    clear_screen()
    play_game()
