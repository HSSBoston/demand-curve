# This program finds a regression line that has the best fit to
# a demand curve that is expressed with 5 data points. See  
# priceList an demandList for those data points. This program
# also draws the original demand curve and regression line. 

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def linearFunction(price, a, b):
    return a * price + b

priceList =[0, 4, 6, 10, 16]
demandList = [4.5, 3, 2.25, 0.75, 0]

param, cov = curve_fit(linearFunction, priceList, demandList)
a = param[0]
b = param[1]
print("Slope: " + str(a))
print("Y-intercept: " + str(b))

regressionList =[]

for p in priceList:
    regressionList.append(a * p + b)

plt.plot(priceList, demandList, marker=".", label="Demand curve")
plt.plot(priceList, regressionList, marker=".", label="Regression line")

plt.xlabel("Price ($)")
plt.ylabel("Demand ($)")
plt.grid()
plt.legend()
plt.show()


