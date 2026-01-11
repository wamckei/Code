import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
print(np.sum(x))
print(np.mean(x))
print(np.min(x))
print(np.max(x))
print(np.std(x))


# Arithmatic on 2-deminisional Arrays

y = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(np.sum(y,0))
print(np.sum(y,1))