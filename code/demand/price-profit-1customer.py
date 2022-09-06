# This program constructs a demand curve (linear line) from
# two data points, (x1, y1) and (x2, y2): d = a * p + b.
# Then, it calculates price-profit relationship by considering
# the cost "c". It finally draws the relationship on a price-profit
# coordinate plane.

import matplotlib.pyplot as plt

x1 = 4
y1 = 4
x2 = 6
y2 = 1

a = (y2-y1) / (x2-x1)
b = y1 - a * x1
print("d = " + str(a) + " * p　+　" + str(b))

p = 0
priceList = []
profitList = []
d = a * p + b
c = 3.21

while d > 0:
    d = a * p + b
    revenue = p * d
    profit =  d * (p - c)
    print("price=" + str(p) + " demand=" + str(d) +
          " revenue=" + str(revenue) + " profit=" + str(profit))
    priceList.append(p)
    profitList.append(profit)
    p = p + 0.25

plt.plot(priceList, profitList, marker=".")
plt.xlabel("Price ($)")
plt.ylabel("Profit ($)")
plt.grid()
plt.show()
