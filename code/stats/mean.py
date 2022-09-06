prices = [7.49, 7.49, 9.98, 6.00, 7.27, 6.65, 6.65, 4.99, 14.26, 9.90, 7.98]

sum = 0
for price in prices:
    sum = sum + price

mean = sum / len(prices)
print("Mean price: " + str(mean))