import math
print("This program is going to calculate the area and circumference of a circle")
radius = float(input("Type the radius of the circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print("Area = ", round(area,2))
print("Circumference = ", round(circumference,2))
