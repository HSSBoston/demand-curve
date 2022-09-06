import matplotlib.pyplot as plt
 
prices = [7.49, 7.49, 9.98, 6.00, 7.27, 6.65, 6.65, 4.99, 14.26, 9.90, 7.98]

plt.xlabel("Price ($)")
plt.ylabel("Frequency")

plt.hist(prices, bins=range(0, 16, 1))

plt.xticks(range(0,16,1))
plt.yticks(range(0, 5, 1))
plt.grid()
plt.show()