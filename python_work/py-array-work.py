#! /usr/bin/python3
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import sys

x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)


print (y)
print("---------------------------------")
print(y_with_nan)
print("---------------------------------")
print(z)
print("---------------------------------")
print(z_with_nan)
print("---------------------------------")


#mean value
mean_ = sum(x) / len(x)

print("mean value for x")
print(mean_)


#alternarte method using pythong statistics to get mean of x

meanpystat = statistics.mean(x)
print("mean of X using py stat")
print(meanpystat)

#alternarte method using python statistics to get mean of x_with_nan

meanpystat = statistics.mean(x_with_nan)
print("mean of x_with_nan using py stat")
print(meanpystat)

#alternarte method using numPY to get mean of y
meanpystat = np.mean(y)
print("mean of y using numPY")
print(meanpystat)


