weight = 84
height = 1.65

bmi = weight / height**2
# Obv. converts to interger
print(int(bmi))     # output: 30

# This function uses rounding 
print(round(bmi))       #output: 31

# Round to a chosen decimal point
print(round(bmi, 3))        #output: 30.854

# Assignment Operator - +=, -=, *=, /=

# F-string - Handles type conversions automatically !
print(f"your bmi is: {bmi}")

