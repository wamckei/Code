import random

# Lists of Friends
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel", "Becky"]
# Setting a variable count to =
count = 0

# Counting the number of indexes in list
for x in friends:
    count +=1
# Or use print(len(friends))    #to get 6 as the length and use minus 1 to account for starting at 0 as done below. 
# Or  do this: y = len(friends)

# Generating a random number for the index 0 - 5, the -1 to account for list's index starting with 0 and not 1
rand_friend = random.randint(0 , count - 1)
# Print who pays
print(f"And the winner is: {friends[rand_friend]} !!")

# Another option (RTFM)
# print(random.choice(friends))




