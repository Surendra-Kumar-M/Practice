import math
def Shapes():
    def Area():
        def square(): #Square
            a=int(input("\nEnter the Size of the Square's Side : "))
            print("The Area of the Square : ",a*a,"sq.units")
            
        def rectangle(): #Rectangle
            l=int(input("\nEnter the Size of the Rectangle's Length : "))
            w=int(input("Enter the Size of the Rectangle's Width : "))
            print("The Area of the Rectangle : ",l*w,"sq.units")
            
        def triangle(): #Triangle
            h=int(input("\nEnter the Size of the Triangle's Height : "))
            b=int(input("Enter the Size of the Triangle's Base : "))
            a=0.5*b*h
            print("The Area of the Triangle : ",a,"sq.units")
            
        def circle():  #Circle
            r=int(input("\nEnter the Radius of the Circle : "))
            a=(math.pi*(r**2))
            print("The Area of the Circle : ",a,"sq.units")
            
        print("\nFind the Area of the Shape")
        print("Select the Shape")
        print("\n\t1.SQUARE \n\t2.RECTANGLE \n\t3.TRIANGLE \n\t4.CIRCLE \n\t5.CLOSE")
        Ch=int(input("\nSELECT OPTION : "))

        if(Ch==1):
            square()
        elif(Ch==2):
            rectangle()
        elif(Ch==3):
            triangle()
        elif(Ch==4):
            circle()
        elif(Ch==5):
            return Shapes()
            
    def Perimeter():

        def square(): #Square
            a=int(input("\nEnter the Size of the Square's Side : "))
            print("The Perimeter of the Square : ",a*4,"units")
            
        def rectangle(): #Rectangle
            l=int(input("\nEnter the Size of the Rectangle's Length : "))
            w=int(input("Enter the Size of the Rectangle's Width : "))
            print("The Perimeter of the Rectangle : ",(l+w)*2,"units")
            
        def triangle(): #Triangle
            t1=int(input("\nEnter the Size of the Triangle's 1st Side : "))
            t2=int(input("Enter the Size of the Triangle's 2nd side : "))
            t3=int(input("Enter the Size of the Triangle's 3rd side : "))
            print("The Perimeter of the Triangle : ",t1+t2+t3,"units")
            
        def circle():  #Circle
            r=int(input("\nEnter the Radius of the Circle : "))
            a=(math.pi*(r*2))
            print("The Perimeter of the Circle : ",a,"units")

        print("\nFind the Perimeter of the Shape")
        print("Select the Shape")
        print("\n\t1.SQUARE \n\t2.RECTANGLE \n\t3.TRIANGLE \n\t4.CIRCLE \n\t5.CLOSE")
        Ch=int(input("\nSELECT OPTION : "))

        if(Ch==1):
            square()
        elif(Ch==2):
            rectangle()
        elif(Ch==3):
            triangle()
        elif(Ch==4):
            circle()
        elif(Ch==5):
            return Shapes()
        
    Ch=input("CALCULATE AREA OR PERIMETER OF SHAPES\nA or P : ")
    if(Ch=='A'):
        Area()
    elif(Ch=='P'):
        Perimeter()

    C=input("\nDo you Want to Continue.....\nY or N : ")
    if(C=='Y'):
        Shapes()
        
Shapes()
