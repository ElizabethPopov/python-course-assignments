from math import pi
import sys

radius = float(sys.argv[1])

if len(sys.argv) != 2:
    print("You should provide a single numerical value for the radius.")
    sys.exit(1)

area = pi*(radius)**2 
circumeference = 2*pi*radius

print(f"The area of your circle: {round(area,3)}\nThe circumference of your circle: {round(circumeference,3)}")