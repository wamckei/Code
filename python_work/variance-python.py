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

#Calculating Variance with pure python
n = len(x)
mean_ = sum(x) / n
var_ = sum((item - mean_)**2 for item in x) / (n - 1)
print("Calculating Variance with pure python")
print(var_)

#Calculating variance with py stat
vari_pystat = statistics.variance(x, mean_)
print("Calculating variance with py stat")
print(vari_pystat)

