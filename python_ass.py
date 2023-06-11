import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Two distinct real roots:")
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("One real root:")
        print("Root:", root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print("Two complex roots:")
        print("Root 1:", real_part, "+", imaginary_part, "i")
        print("Root 2:", real_part, "-", imaginary_part, "i")

# Example usage:
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

find_roots(a, b, c)
