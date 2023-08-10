import math

#no parameter no return
def square():
    a=int(input("Enter the Side Value of a Square : "))
    print("Area of the Square is ",a**2)

#With parameter no return
def rectangle(l,b):
    print("Area of the Rectangle is ",l*b)

#no parameter With return
def circle():
    r=float(input("Enter the Radius of the Circle : "))
    return (math.pi*(r**2))

# With parameter With return
def triangle(ba,h):
    return (0.5*ba*h)

#Calling Section
print("\t\tSQUARE")
print(square())

print("\n\t\tRECTANGLE")
l=int(input("Enter the Length of the Rectangle : "))
b=int(input("Enter the Breadth of the Rectangle : "))
print(rectangle(l,b))

print("\n\t\tCircle")
print("Area of the Circle is ",circle())

print("\n\t\tTriangle")
ba=int(input("Enter the base value of the Triangle : "))
h=int(input("Enter the Height of the Triangle : "))
print("Area of the Triangle is ",triangle(ba,h))
