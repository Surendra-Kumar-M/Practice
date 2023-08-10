import math
class Area():

    def square(self): #Square
        a=int(input("Enter the length of the side of the Square : "))
        return a*a
    
    def rectangle(self,l,w): #Rectangle
        return(l*w)
    
    def triangle(self,b,h): #Triangle
        a=0.5*b*h
        print("Area of the Triangle : ",a,"sq.units\n")
        
    def circle(self):  #Circle
        r=float(input("Enter the Radius of the Circle : "))
        a=(math.pi*(r**2))
        print("Area of the Circle : ",a,"sq.units\n")
        
    def rhombus(self,a,b): #Rhombus
        return (0.5*a*b)
    
A=Area()    #Object Creation
print("\t\tSquare")
print("Area of the Square :",A.square(),"sq.units\n")

print("\t\tRectangle")
l=float(input("Enter the Length of the Rectangle : "))
w=float(input("Enter the Width of the Rectangle : "))
print("Area of the Rectangle : ",A.rectangle(l,w),"sq.units\n") 

B=Area()
print("\t\tTriangle")
h=float(input("Enter the Height of the Triangle : "))
b=float(input("Enter the Base of the Triangle : "))
B.triangle(h,b)

print("\t\tCircle")
B.circle()

C=Area()
print("\t\tRhombus")
d1=float(input("Enter the Diagonal-1 length of the Rhombus : "))
d2=float(input("Enter the Diagonal-2 length of the Rhombus : "))
print("Area of the Rectangle : ",C.rhombus(d1,d2),"sq.units\n")

D=Area()
print("\t\tSquare")
print("Area of the Square :",D.square(),"sq.units\n")
print("\t\tRectangle")
l=float(input("Enter the Length of the Rectangle : "))
w=float(input("Enter the Width of the Rectangle : "))
print("Area of the Rectangle : ",D.rectangle(l,w),"sq.units\n") 
print("\t\tTriangle")
h=float(input("Enter the Height of the Triangle : "))
b=float(input("Enter the Base of the Triangle : "))
D.triangle(h,b)
print("\t\tCircle")
D.circle()
print("\t\tRhombus")
d1=float(input("Enter the Diagonal-1 length of the Rhombus : "))
d2=float(input("Enter the Diagonal-2 length of the Rhombus : "))
print("Area of the Rectangle : ",D.rhombus(d1,d2),"sq.units\n")

