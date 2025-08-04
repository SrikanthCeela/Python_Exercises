# WAP to check the euclidean distance between two coordinates

import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

x = (x1, y1)
y = (x2, y2)

ed = round(math.sqrt((x2-x1)**2 + (y2-y1)**2),2)

print(f"The euclidean distance between {x} and {y} is {ed}")