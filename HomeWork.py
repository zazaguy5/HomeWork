from math import pi

def square_area(l):
    return l*l

def triangle_area(h, b):
    return 0.5*(h*b)

def circle_area(r):
    return 2*pi*r

def cylinder_volume(h, r):
    return (2*pi*r)*(h+r)

def circle_volume(r):
    return 4/3*(pi*r*r*r)

def cubic_volume(h, l, w):
    return h*l*w

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

radius_cylinder = int(input("Enter radius of cylinder: "))
height_cylinder = int(input("Enter height of cylinder: "))
area_cylinder = cylinder_volume(height_cylinder, radius_cylinder)
print(f"Volume of cylinder is: {radius_cylinder}")

radius_circle_volume = int(input("Enter raduis of circle: "))
area_volume = circle_volume(radius_circle_volume)
print(f"Volume of cicle is: {area_volume}")

cubic_height = int(input("Enter height of cubic: "))
cubic_lenght = int(input("Enter length of cubic: "))
cubic_wide = int(input("Enter wide of cubic: "))
volume_cubic = cubic_volume(cubic_height, cubic_lenght, cubic_wide)
print(f"Volume of cubic is: {volume_cubic}")