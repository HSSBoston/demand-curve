# Construct a demand curve (linear line) from two data points: 
# (x1, y1) and (x2, y2) and draw it on a price-demand coordinate plane.

import matplotlib.pyplot as plt

x1 = 4
y1 = 4
x2 = 6
y2 = 1

a = (y2-y1) / (x2-x1)
b = y1 - a * x1
print("d = " + str(a) + " * p + " + str(b))

p = 0
pList = []
dList = []
d = a * p + b

while d > 0:
    d = a * p + b
    pList.append(p)
    dList.append(d)
    p = p + 0.25

plt.plot(pList, dList, marker=".")
plt.xlabel("Price ($)")
plt.ylabel("Demand (lb)")
plt.grid()
plt.show()
