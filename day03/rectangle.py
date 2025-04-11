import sys

if len(sys.argv) != 3:
    print("You should provide two numerical values for the height and width.")
    sys.exit(1)

try:
    height = float(sys.argv[1])
    width = float(sys.argv[2])
except ValueError:
    print("The height and width should be numbers.")
    sys.exit(1)


area = height * width
perimeter = 2 * (height + width)

print(f"The area of your rectangle is: {round(area,3)}\nThe perimeter of your rectangle is: {round(perimeter,3)}")