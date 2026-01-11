# This is one way 
def double(x):
    return x * 2
print(double(5))

# Use Lambda to avoid creating unnecessary functions like above
double = lambda x: x * 2
print(double(5))
