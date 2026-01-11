# Treasure Island game 
print("Welcome to Treasure Island. Your mission is to find the treasure!")

# vars 
direction = input("You run into a cliff, which way are you going to turn? Left or Right ").lower()

# Logic for game

if direction == "left":
    lake_cross = input("You approach an Ocean and you can either swim or wait to see if there is alternative passage ").lower()
    if lake_cross == "wait":
        door_select = input("You approach a weird house with multiple doors, which door will you choose? The Red, Blue or Yellow? ").lower()
        if door_select == "red":
            print("You choose Red, the room is full of toxic waste, you dead, Game Over")
        elif door_select == "blue":
            print("You are struck by lightening and died, Game Over")
        elif door_select == "yellow":
            print("You found the treasure and WIN!!! Good for You!")
    else:
        print("You chose to swim and were attacked by feral kittens and died, Game over")
else:
    print("You fell off the clif butcause you are a butter finger, brilliant. Enjoy Death. Game Over!")




