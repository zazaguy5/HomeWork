def triangle_area(h, b):
    return 0.5*(h*b)

height = int(input("Enter height of triangle: "))
base = int(input("Enter base length of triangle: "))
area_triangle = triangle_area(height, base)
print(f"Area of triangle is: {area_triangle}")