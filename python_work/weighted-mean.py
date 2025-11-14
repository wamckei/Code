#! /usr/bin/python3
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import sys


#Arrays defined
x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)



#Weighted Mean --------------------------------------------------------------------------------------------------
wmean = sum(w[i]* x[i] for i in range(len(x))) / sum(w)
print("Weighted mean using range")
print(wmean)

wmeanzip = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
print("weighted mean using zip")
print(wmeanzip)

y, z, w = np.array(x), pd.Series(x), np.array(w)
wmeannumpy = np.average(y, weights=w)
print("weighted mean using numPY")
print(wmeannumpy)

#Harmonic mean --------------------------------------------------------------------------------------------------
harmean  = len(x) / sum(1 / item for item in x)
print("harmonic mean using nativ Py stat")
print(harmean)

scipyharmean = scipy.stats.hmean(y)
print("harmonic mean using scipy stats")
print(scipyharmean)

#Geometric Mean --------------------------------------------------------------------------------------------------
#Calculate geometric mean using nativ Py stat

geomeanpystat = 1
for item in x:
    geomeanpystat *= item

geomeanpystat **= 1 / len(x)
print("Geometric mean calculated using nativ Py stat")
print(geomeanpystat)

#Geometric mean calculated using statistics.geometric_mean, which convets all values to floating-point numbers

gmean = statistics.geometric_mean(x)
print("Geometric mean calculated using statistics.geometric_mean, which convets all values to floating-point numbers")
print(gmean)

#geometric mean calculated with scipy
scipygmean = scipy.stats.gmean(y)
print("geometric mean calculated with scipy")
print(scipygmean)

#for nan, 0 and negative values.
nanbrokengmean = statistics.geometric_mean(x_with_nan)
print("geometric mean calculated with nan values using nativ py stat - will only produce nan output")
print(nanbrokengmean)


#Median --------------------------------------------------------------------------------------------------

n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index-1] + x_ord[index])

print("Calculating median value using python nativ py stat")
print(median_)


#Low and High elements when they are even
lowmedian = statistics.median_low(x[:-1])
print("calculated using py stat median_low")
print(lowmedian)

highmedian = statistics.median_high(x[:-1])
print("calculated using py stat median_high")
print(highmedian)

#Unlike most other functions from the Python statistics library, median(), median_low(), and median_high() don’t return nan when there are nan values among the data points

nanmedium = statistics.median(x_with_nan)
print("Median calculated when nan value included with py stat")
print(nanmedium)

nanmedianlow = statistics.median_low(x_with_nan)
print("Median calculated when nan value included with py stat using median_low")
print(nanmedianlow)

nanmedianhigh = statistics.median_high(x_with_nan)
print("Median calculated when nan value included with py stat using median_high")
print(nanmedianhigh)

#Calculate median with numPY
mediannumpy = np.median(y)
print("Calculating median with numPy")
print(mediannumpy)

#median calculated when nan values presant using nanmedian with odd data set
nanmediannumpy =  np.nanmedian(y_with_nan)
print("Median value calculated when nan values exist on odd data sets")
print(nanmediannumpy)

#median calculated when nan values presant using nanmedian with even data set
nanmediannumpyeven =  np.nanmedian(y_with_nan[:-1])
print("Median value calculated when nan values exist on even data sets")
print(nanmediannumpyeven)



