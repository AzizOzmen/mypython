# Find the Perimeter of a Rectangle
# Create a function that takes
# length and width and finds the perimeter of a rectangle.

def find_perimeter(side1, side2):
    perimeter = (side1 + side2) * 2
    print(perimeter)
    return (side1 + side2) * 2

find_perimeter(6, 7)  # ➞ 26
find_perimeter(20, 10)  # ➞ 60
find_perimeter(2, 9)  # ➞ 22