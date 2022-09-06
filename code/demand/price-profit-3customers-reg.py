# This program uses a regression curve
#   d = 56.80874189396707 / p - 4.843449714302733
# as a demand curve. Then, this program calculates
# price-profit relationship by considering the cost "c".
# It finally draws the relationship on a price-profit
# coordinate plane.

import matplotlib.pyplot as plt

def demand(price):
    if price >= 0 and price <= 6.5:
        return -2.875 * price + 21.75
    elif price > 6.5 and price <= 9:
        return -0.875 * price + 8.75
    elif price > 9:
        return -0.125 * price + 2        

p = 3.0
priceList = []
profitList = []
d = 56.80874189396707 / p - 4.843449714302733
c = 3.21

while d >= 0:
    d = 56.80874189396707 / p - 4.843449714302733
    revenue = p * d
    profit =  d * (p - c)
    print("price=" + str(p) + " demand=" + str(d) +
          " revenue=" + str(revenue) + " profit=" + str(profit))
    priceList.append(p)
    profitList.append(profit)
    p = p + 0.25

realProfitList = []
for p in priceList:
    d = demand(p)
    realRevenue = p * d
    realProfit = d * (p - c)
    realProfitList.append(realProfit)

plt.plot(priceList, realProfitList, marker="s",
         label="Profit")
plt.plot(priceList, profitList, marker=".",
         label="Estimated profit")

plt.xlabel("Price ($)")
plt.ylabel("Profit ($)")
plt.grid()
plt.legend()
plt.show()

