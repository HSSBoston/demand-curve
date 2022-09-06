# This program uses a regression line
#   d = -0.2862903225834508 * p + 4.161290322587539
# as a demand curve. Then, this program calculates
# price-profit relationship by considering the cost "c".
# It finally draws the relationship on a price-profit
# coordinate plane.

import matplotlib.pyplot as plt

p = 0
priceList = []
profitList = []
d = -0.2862903225834508 * p + 4.161290322587539
c = 3.21

while d > 0:
    d = -0.2862903225834508 * p + 4.161290322587539
    revenue = p * d
    profit =  d * (p - c)
    print("price=" + str(p) + " demand=" + str(d) +
          " revenue=" + str(revenue) + " profit=" + str(profit))
    priceList.append(p)
    profitList.append(profit)
    p = p + 0.25

plt.plot(priceList, profitList, marker=".")
plt.xlabel("Price")
plt.ylabel("Profit")
plt.grid()
plt.show()

