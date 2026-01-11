# List of states
usa_states = ["Delaware", "Pennsylvania", "Alabama", "Mississippi", "Washington", "Florida", "Arazona", "New Mexico"]
# Prints element in index 2
print(usa_states[2])    # Prints "Alabama"

# Negative index, counts from the back (reverse)
print(usa_states[-2])   # Prints "Arazona"

# Make edits on list 
usa_states[2] = "Bama"  # Changes index 2 "Alabama" to "Bama"
print(usa_states[2])

# Add an item to a list 
usa_states.append("New York")
print(usa_states)

# Extend the list with another list
usa_states.extend(["Colorado", "Ohio", "Texas", "North Carolina", "South Carolina"])
print(usa_states)

######################################
# Nested Lists
list1 = ["pear", "Apple", "Grapes"]
list2 = ["Pizza", "Lemons", "Green"]

# Creates a list of 2 lists 
mixed = [list1, list2]

print(mixed)

print(mixed[1][1])   # Prints Lemons - as the mixed list uses the second argument (list2) and the 1st index of that list.




