from math import pi

radius = float(input("Enter the radius of the circle you want to calculate: "))

area = pi*(radius)**2 
circumeference = 2*pi*radius

print(f"The area of your circle: {round(area,3)}\nThe circumference of your circle: {round(circumeference,3)}")
