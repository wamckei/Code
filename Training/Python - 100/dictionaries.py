# Dictionary defination
fruits = {
    "Apple": "Red", 
    "Bananna": "Yellow", 
    "Grapes": "Green"
    }

# Reference data in a dict via the key, similar to lists and indexes, the key reference must match the key data type in the dict. 
print(fruits["Apple"])

# Add data to a dict, can also be used to edit a value when calling an existing key
fruits["Orange"] = "Orange"
print(fruits)

# Empty out a dict 
#fruits = {}

# Loop through a dictionary
for key in fruits:
    print(key)
    print(fruits[key])

# Nesting *************************

# dictionary = {
#     key: [list],
#     key: {dict},
# }    

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgrad", "Berlin"],
}

# Print specific index in a list embeded in a dict
print(travel_log["France"][1])

# Nested List
nested_list = ["A", "B", ["C", "D"]]

# Print "D" from the nested list
print(nested_list[2][1])

# Nested dictionary with in a dictionary
t_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 8
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "num_times_visited": 5
    },
}

# Print Stuttgart from this nested list in a nested dict. 
print(t_log["Germany"]["cities_visited"][2])






