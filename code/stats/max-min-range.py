prices = [7.49, 7.49, 9.98, 6.00, 7.27, 6.65, 6.65, 4.99, 14.26, 9.90, 7.98]

min = prices[0]
for x in range(len(prices)):
    if prices[x] < min:
        min = prices[x]
print("Minimum price:" + str(min))

max = prices[0]
for y in range(len(prices)):
    if prices[y] > max:
        max = prices[y]
print("Maximum price: " + str(max))

range = max - min
print("Range:" +str(range))