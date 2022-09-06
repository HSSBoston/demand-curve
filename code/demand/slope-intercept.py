# Construct a line (linear function) from two data points: 
# (x1, y1) and (x2, y2). The variables "a" and "b" are slope 
# and y-intercept.

x1 = 8
y1 = 1
x2 = 4
y2 = 1.5

a = (y2-y1) / (x2-x1)
b = y1 - a * x1

print("d = " + str(a) + " * p + " + str(b))