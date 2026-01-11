import numpy as np

# Create simple Array
x = np.arange(10)

print(x)

print(x[2:7])
print (x[:5])

# 2-demensional array
y = np.array([[1,2,3,4], [5,6,7,8]])
print(y[0]) #first Row

# Print first index from all colomuns
print(y[:,1])

z = np.arange(12)
reshaped = z.reshape(3,4)

print(reshaped)

flat = reshaped.flatten()
print(flat)


