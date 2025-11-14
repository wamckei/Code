#! /usr/bin/python3
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import sys

#Statastica Mode

u = [2, 3, 2, 8, 12]
mode_ = max((u.count(item), item) for item in set(u))[1]
print("Calculates the Mode of an array")
print(mode_)

