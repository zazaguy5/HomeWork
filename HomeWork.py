from math import pi

def square_area(l):
    return l*l

def triangle_area(h, b):
    return 0.5*(h*b)

def circle_area(r):
    return 2*pi*r

height = int(input("Enter height of triangle: "))
base = int(input("Enter base length of triangle: "))
area_triangle = triangle_area(height, base)
print(f"Area of triangle is: {area_triangle}") 

side_length = int(input("Enter height of triangle: "))
area_square = square_area(side_length)
print(f"Area of square is: {area_square}")

radius = int(input("Enter radius of circle: "))
area_circle = circle_area(radius)
print(f"Area of circle is: {area_circle}")
