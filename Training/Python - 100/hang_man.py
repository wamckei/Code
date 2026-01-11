import random
from hangman_art import hangman, logo
from hangman_words import word_list

# User lives
life = 6

# Print logo
print(logo)

# Pick a random word from the list
choosen_word = random.choice(word_list)
print(choosen_word)


# While loop to continue game until game over
game_over = False
correct_letters = []

# Iterate through until life = 0 and break out of loop
while not game_over:

    # Update user on lives left 
    print(f"************************{life}/6 LIVES LEFT*******************************")

    # Ask user to imput a guess of a letter in the word, assign it and make it lowercase
    user_guess = input("Guess a letter in the word: ").lower()

    if user_guess in correct_letters:
        print(f"Letter already guessed: {user_guess}")

    # Create an empty string to act as a place holder
    placeholder =  " "
    wrd_len = len(choosen_word)

    # Count the number of letters in  the chosen word and place "-" into empty string
    for position in range(wrd_len):
        placeholder += "_"

    # Compare guessed letter against word to see if it exists, if it exists then place the letter into a variable in the proper position
    display = " "

    # Check to see if the users input matches a letter in the word. If not check that user input against the list word that retains history of correct letters, else add underscores 
    for letter in choosen_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # If the user guess isn't in the retained list of correct letters "chosen_word" then reduce life by 1, when life = 0 end game and show full hangman ASCII art
    if user_guess not in choosen_word:
        life -= 1
        print(f"You guessed {user_guess}, which is not in the word. You LOSE A LIFE!!!")
        if life == 0:
            game_over = True
            print("***********************You Lose!*********************")
            print(f"The word was: {choosen_word}")

    # If there are no underscores left in display variable, The game is won
    if "_" not in display:
        game_over = True 
        print("***********************You Win!************************")

    # Print the ASCII art at the position equal to the number of lives left
    print(hangman[life])


