from calculator_app_logo import logo

print(logo)

# Functions to add, subtract, multiply and divide
def add(x1, x2):
    return x1 + x2

def subtract(x1, x2):
    return x1 - x2

def multiply(x1, x2):
    return x1 * x2

def divide(x1, x2):
    return x1 / x2

# Difine dictionary to store all of the operator functions 
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator():

    # print(operations["*"](4,8))

    answer = True
    first_num = float(input("Enter the first number of the calculation:  "))

    while answer:
        for symbol in operations:
            print(symbol)

        operator = input("Enter the operator that represents the calculation you wish to use:  ")
        second_num = float(input("Enter the second number of the calculation:  "))
        calc = operations[operator](first_num,second_num)
        print(f"{first_num} {operator} {second_num}= {calc}")
        
        continue_calc = input("Do you wish to continue working with the previous result? y or n, If you wish to quite type 'quit' :  ").lower()

        if continue_calc == "y":
            first_num = calc
        elif continue_calc == "n":
            answer = False
            calculator()
        elif continue_calc == 'quit':
            print("Good By!!!")
            answer = False

calculator()