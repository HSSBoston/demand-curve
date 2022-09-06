prices = [7.49, 7.49, 9.98, 6.00, 7.27, 6.65, 6.65, 4.99, 14.26, 9.90, 7.98]

# Sorting prices in ascending order with "bubble sort" algorithm
#
for round in range(len(prices)-1):
    for x in range(len(prices)-1):
        if prices[x] > prices[x+1]:
            leftNum = prices[x]
            rightNum = prices[x+1]
            prices[x] = rightNum
            prices[x+1] = leftNum
print("Sorted list: " + str(prices))

# Finding the median value
#
if len(prices) % 2 == 0:
    a = int(len(prices) / 2)
    b = int(len(prices) / 2 + 1)
    median = (prices[a-1] + prices[b-1]) / 2
    print("Median price: " + str(median))
else:
    a = len(prices) // 2 + 1
    median = prices[a-1]
    print("Median price: " + str(median))
