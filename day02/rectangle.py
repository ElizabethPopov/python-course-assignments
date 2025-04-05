height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = height * width
perimeter = 2 * (height + width)

print(f"The area of your rectangle is: {round(area,3)}\nThe perimeter of your rectangle is: {round(perimeter,3)}")