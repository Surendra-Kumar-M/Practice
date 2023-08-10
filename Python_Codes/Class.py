import math
class Area():
    def square(self,a): #Square
        return (a**2)
    def rectangle(self,l,w): #Rectangle
        return(l*w)
    def triangle(self,b,h): #Triangle
        a=0.5*b*h
        return a
    def circle(self,r):  #Circle
        a=(math.pi*(r**2))
        return a

A=Area()   #Object Creation

print("\t\tSquare")
a=float(input("Enter the side of the Square : "))
print("Area of the Square : ",A.square(a),"sq.units\n") #Method Calling

print("\t\tRectangle")
l=float(input("Enter the Length of the Rectangle : "))
w=float(input("Enter the Width of the Rectangle : "))
print("Area of the Rectangle : ",A.rectangle(l,w),"sq.units\n") #Method Calling

print("\t\tTriangle")
h=float(input("Enter the Height of the Triangle : "))
b=float(input("Enter the Base of the Triangle : "))
print("Area of the Triangle : ",A.triangle(b,h),"sq.units\n")  #Method Calling

print("\t\tCircle")
r=float(input("Enter the Radius of the Circle : "))
print("Area of the Circle : ",A.circle(r),"sq.units")   #Method Calling
        
        
