# Error handling
#trigger an error 

#try:

#    numerator = input("Enter the Numerator: ")
#    denominator = input("Enter the denomenator: ")

    # if devide by 0 it throws an error (obv..)
#    output  = numerator / denominator
#except ZeroDivisionError:
#    print("Error: You can't divide by 0")
#except TypeError:
#    print("Error: Invalid input type. Please enter numbers")


try: 
    age = input("Enter the age: ")
    if int(age) < 0:
        raise ValueError("Age is negative, please enter a valid age")
except TypeError:
    print("Error: Invalid input type. Please enter numbers")
except ValueError:
    print("Error: Invalid value, Please enter a valid age. ")  #output with a negative number - >  Error: Invalid value, Please enter a valid age. 