# # # Single parameter function
def my_greet(name):
    print(f"Hello {name}")
    print(f"How is your day {name}?")
    print("Lovely weather out today!")
answer = input("Welcome, what is your name? ")
my_greet(answer)

# # # Multi-parameter functions - arguments are associated by order
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}")
greet_with("Will", "Denmark")

# # # Keyword Arguments - Multi-parameter functions - assigning the argument to a parameter does not consider order
def key_greet(name, location, age):
    print(f" Greetings, {name}")
    print(f"How is the weather in {location}")
    print(f"Must be nice to be {age} young")
key_greet(location="Denmark", name="Will", age="47")


# # # Functions with output
# # # ex.
def my_function():
    return 3 * 6
#function call and asigning the returned value
ouput = my_function()   # output has a value of 18

# # Use of the title() function, sets the first character of a word to upper case
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

corrected_name = format_name(first_name, last_name)
print(corrected_name)

#Function calls with returned function data
def function_1(text):
    return text + " " + text

def function_2(text):
    return text.title()

formatted_text = function_2(function_1("hElLo"))
print(formatted_text)

# Functions which return multiple values - comma seperated
def my_function3(text1, text2):
    conversion_1 = text1.upper()
    conversion_2 = text2.upper()
    return conversion_1, conversion_2

# Docstrings ********************

def my_function4(text1, text2):
    """ Take two words and converts all characters to upper case"""  #3 quotes
    conversion_1 = text1.upper()
    conversion_2 = text2.upper()
    return conversion_1, conversion_2
my_function4("Hello", "World")  #scroll over the function to see the docstring you entered - this will provide more information on the function in the pop up window. 

# Alias for functions
def fun_ction(n1, n2):
    return n1 + n2

# Set alias for function
some_alias = fun_ction

# Call function under new alias
some_alias(2,3)
    

