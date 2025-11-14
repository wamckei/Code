#! /usr/bin/python3
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import sys

#Variables 
x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

#calculate the mean
n = len(x)
mean_ = sum(x) / n

#Calculate using Py stat
std_  =statistics.stdev(x, mean_)
print("Calculate standard deviation using py stat")
print(std_)


#calculate variance 

var_ = sum((item - mean_)**2 for item in x) / (n - 1)

#calculate skewness
skew_ = (sum((item - mean_)**3 for item in x)
         * n / ((n - 1) * (n - 2) * std_**3))
print("Calculate Skewness")
print(skew_)

#Calculate Skewness with Pandas
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print("Calculate skewness with Pandas")
print(z.skew())






