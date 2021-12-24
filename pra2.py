import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import Counter
import numpy as np
import statistics
import sys
import math
from scipy.stats import kurtosis
def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance
print("------------------------------------------------------------------------")
print("---------------------------------Subject:Java----------------------------")
data = list(map(int,input("Enter Marks Of Students :").split(" ")))
print("Data Successfully Enter")
n = len(data)
mean = sum(data) / n
data.sort()
if n % 2 == 0:
    median1 = data[n // 2]
    median2 = data[n // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = data[n // 2]
var = variance(data)
s= math.sqrt(var)
skw=3*(mean-median)/s
print("Skewness=",skw)
if skw == 0:
    print("normally distributed")
elif skw<0:
    print("Positive Skew")
    print("more weight in the right tail of the distribution.")
elif skw>0:
    print("Negaitive Skew")
    print("more weight in the left tail of the distribution.")
else:
    print("------------------------------------------------------------")
k=kurtosis(data,fisher=False)
print("kurtosis=",k)
if k==3:
    print("Normal Distribution")
elif k<3:
    print("playkurtic")
elif k>3:
    print("leptokurtic")
else:
    print("------------------------------------------------------------")
x = np.arange(1, 18, 0.10)
plt.plot(x, norm.pdf(x, 0, 1),label="Sample Data")
plt.title("Java")
plt.plot(x, norm.pdf(x,mean),label="Marks")
#plt.plot(x,norm.pdf(x,skw),label="Skewness")
#plt.plot(x,norm.pdf(x,k),label="kurtosis")
plt.ylabel("Normal Distribution")
plt.xlabel("Marks")
plt.legend()
plt.show()


