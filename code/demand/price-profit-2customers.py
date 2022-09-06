# This program expresses a demand curve with 2 linear functions;
# See the demand() function. Then, this program calculates
# price-profit relationship by considering the cost "c". It finally
# draws the relationship on a price-profit coordinate plane.

import matplotlib.pyplot as plt

def demand(p):
    if p >= 0 and p <= 10:
        d = -0.375 * p + 4.5
    else:
        d = -0.125 * p + 2
    return d

p = 0
priceList = []
profitList = []
d = demand(p)
c = 3.21

while d > 0:
    d = demand(p)
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

