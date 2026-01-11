# List for using loops below
cars = ["mustang", "F-150", "Crosstrek"]

# For loop example
for x in cars:
    print(x)
    print(x + " blue")


# Range function - if you want to generate a range of #'s to loop through
for x in range(1, 10):  #can use a 3rd argument for stepping, example  range(1, 10, 3) will print 1, 4, 7, 10
    print(x)

# Gauss Challenge - sum all the numbers from 1 - 100 (range has to end at 101 as the last number isn't included in range)
y = 0
for i in range(1, 101):
    y += i
print(y)


