# This program finds a regression line and two regression curves
# that have the best fit to a demand curve that is expressed with
# 9 data points. See  priceList an demandList for those data points.
# This program also draws the original demand curve, a regression line
# and regression curves. 

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

priceList = [3.21, 4, 5, 6, 6.5, 7, 8, 9, 16]
demandList = [12.52, 10.25, 7.375, 4.5, 3.0625, 2.625, 1.75, 0.875, 0]

def linearFunction(price, a, b):
    return a * price + b
    
def inversePropFunction(price, a):
    return a/price

def customizedInversePropFunction(price, a, b):
    return a/price + b

param, cov = curve_fit(linearFunction, priceList, demandList)
slope = param[0]
yIntercept = param[1]
print("Slope: " + str(slope) + " Y-intercept: " + str(yIntercept))

param, cov = curve_fit(inversePropFunction, priceList, demandList)
a1 = param[0]
print("a: " + str(a1))

param, cov = curve_fit(customizedInversePropFunction, priceList, demandList)
a2 = param[0]
b = param[1]
print("a: " + str(a2) + " b: " + str(b))

estDemandList1 =[]
for p in priceList:
    estDemandList1.append(slope * p + yIntercept)

estDemandList2 =[]
for p in priceList:
    estDemandList2.append(a1/p)

estDemandList3 =[]
for p in priceList:
    estDemandList3.append(a2/p + b)

plt.plot(priceList, demandList, marker="s",
         label="Demand curve")
plt.plot(priceList, estDemandList1, marker="x",
         label="Regression line (d=a*p + b)")
plt.plot(priceList, estDemandList2, marker="+",
         label="Regression curve (d=a/p)")
plt.plot(priceList, estDemandList3, marker=".",
         label="Regression curve (d=a/p + b)")

plt.xlabel("Price ($)")
plt.ylabel("Demand (lb)")
plt.grid()
plt.legend()
plt.show()


