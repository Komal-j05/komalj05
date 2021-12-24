import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import Counter
import numpy as np
import statistics
import sys
import math
def mean(data):
    n = len(data)
    mean = sum(data) / n
    return mean
def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance
def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev
def mode(data):
    n = len(data)
    da = Counter(data)
    get_mode = dict(da)
    mode = [k for k, v in get_mode.items() if v == max(list(da.values()))]
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "" + ', '.join(map(str, mode))
        return get_mode
def ste(data):
    s = stdev(data)
    se = s / math.sqrt(5)
    return se
def median(data):
    n = len(data)
    data.sort()
    if n % 2 == 0:
        median1 = data[n // 2]
        median2 = data[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = data[n // 2]
    return median
def gra(a,b):
    x = np.arange(1, 18, 0.10)
    plt.plot(x, norm.pdf(x, 0, 1),label="Sample Data")
    plt.plot(x, norm.pdf(x, a ),label="Mean of 1st Data")
    plt.plot(x, norm.pdf(x, b), label="Mean of 2nd Data")
    plt.legend()
    plt.show()
def main():
    print("-----------------------------------------Statiscal Measures-------------------------------------")
    data = list(map(int, input("Enter Data Set 1:   ").split(" ")))
    dt = list(map(int, input("Enter Data Set 2:   ").split(" ")))
    def me():
        print("1.Mean")
        print("2.Median")
        print("3.Mode")
        print("4.Standard Deviation")
        print("5.Variance")
        print("6.Covariance")
        print("7.Corrlatin")
        print("8.Standard Error")
        print("9.Graphical Reprentaion")
        print("10.Exit")
        print("11.Back")
        print("---------------------------------------------------------------")
        ch = int(input("Enter your choice....."))
        if ch != 0 and ch <= 11:
            if ch == 1:
                print("Mean=", mean(data))
                print("-------------------------------------------------------------------------")
            elif ch == 2:
                print("Median=", median(data))
                print("-------------------------------------------------------------------------")
            elif ch == 3:
                print("Mode=", mode(data))
                print("-------------------------------------------------------------------------")
            elif ch == 4:
                print("Standard Deviation=", stdev(data))
                print("-------------------------------------------------------------------------")
            elif ch == 5:
                print("Variance=", variance(data))
                print("-------------------------------------------------------------------------")
            elif ch == 6:
                #dt = list(map(int, input("Enter Another Data Set:   ").split(" ")))
                print("Covariance=", np.cov(data))
                print("--------------------------------------------------------------------------")
            elif ch == 7:
                #dt = list(map(int, input("Enter Another Data Set:   ").split(" ")))
                print("Correlation=", np.corrcoef(data,dt))
                print("-------------------------------------------------------------------------")
            elif ch == 8:
                print("Standard Error=", ste(data))
                print("-------------------------------------------------------------------------")
            elif ch== 9:
                h=statistics.mean(dt)
                gra(mean(data),h)
            elif ch == 10:
                sys.exit()
            if ch == 11:
                main()
        else:
            print("Invalid Input")
            print("--------------------------------------------------------------------------")
        st=input("type y for continue......................")
        if st =="y":
            me()


    me()
main()
