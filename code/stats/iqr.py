prices = [7.49, 7.49, 9.98, 6.00, 7.27, 6.65, 6.65, 4.99, 14.26, 9.90, 7.98]
#prices =[1, 2, 3, 4, 5, 6, 7, 8, 9]
#prices = [1,2,3,4,5,6,7,8,9,10]
#prices = [1,2,3,4,5,6,7,8]

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

if len(prices) % 2 == 0:
    b = int(len(prices) // 2)
    median = (prices[b-1] + prices[b]) / 2
    print("Median (2nd quartile): " + str(median))
    if b % 2 == 0:
        q1 = (prices[int(b / 2) - 1] + prices [int(b / 2)]) / 2
        print("1st quartile: " + str(q1))
        q3 = (prices[b + int(b / 2)] + prices[b + int(b / 2) - 1]) / 2
        print("3rd quartile: " + str(q3))
    else:
        q1 = prices[b - (b // 2 + 1)]
        print("1st quartile: " + str(q1))
        q3 = prices[b + b // 2]
        print("3rd quartile: " + str(q3))
else:
    b = int(len(prices) // 2)
    median = prices[b]
    print("Median (2nd quartile): " + str(median))
    if b % 2 == 0:
        q1 = (prices[int(b / 2) - 1] + prices [int(b / 2)]) / 2
        print("1st quartile: " + str(q1))
        q3 = (prices[b + int(b / 2)] + prices[b + int(b / 2) + 1]) / 2
        print("3rd quartile: " + str(q3))
    else:
        q1 = prices[b - (b // 2 + 1)]
        print("1st quartile: " + str(q1))
        q3 = prices[b + b // 2 + 1]
        print("3rd quartile: " + str(q3))
print("IQR (Interquartile range): " + str(q3 - q1))
