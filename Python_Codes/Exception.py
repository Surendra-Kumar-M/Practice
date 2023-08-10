try:
    h=int(input("Enter the Height of the Triangle : "))
except ValueError:
    print("Enter a Integer value")
    h=int(input("Enter the Height of the Triangle : "))
try:
    b=int(input("Enter the Base of the Triangle : "))
except ValueError:
    print("Enter a Integer value")
    b=int(input("Enter the Base of the Triangle : "))
    a=0.5*h*b    
else:
    a=0.5*h*b 
    print("No Exception\n Area of Triangle",a)
finally:
    print("Execution Success ❤")
print("Area of Triangle",a)

