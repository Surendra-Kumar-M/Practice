#Getting inputs
a=int(input("Enter the mark in English"))
b=int(input("Enter the mark in Tamil"))
c=int(input("Enter the mark in Maths"))
d=int(input("Enter the mark in Science"))
e=int(input("Enter the mark in Social"))
Mark=0
#Checking for valid inputs
if(a>=0 and a<=100):
    Mark+=a
else:
    print("Enter the valid Mark")
    a=int(input("Enter the mark in English"))
    if(a>=0 and a<=100):
        Mark+=a
    else:
        print("Input Error")
        exit()
if(b>=0 and b<=100):
    Mark+=b
else:
    print("Enter the valid Mark")
    b=int(input("Enter the mark in Tamil"))
    if(b>=0 and b<=100):
        Mark+=b
    else:
        print("Input Error")
        exit()
if(c>=0 and c<=100):
    Mark+=c
else:
    print("Enter the valid Mark")
    c=int(input("Enter the mark in Maths"))
    if(c>=0 and c<=100):
        Mark+=c
    else:
        print("Input Error")
        exit()
if(d>=0 and d<=100):
    Mark+=d
else:
    print("Enter the valid Mark")
    d=int(input("Enter the mark in Science"))
    if(d>=0 and d<=100):
        Mark+=d
    else:
        print("Input Error")
        exit()
if(e>=0 and e<=100):
    Mark+=e
else:
    print("Enter the valid Mark")
    e=int(input("Enter the mark in Social"))
    if(e>=0 and e<=100):
        Mark+=e
    else:
        print("Input Error")
        exit()

#Average Calculation
avg=Mark/5
if((a>=40)and(b>=40)and(c>=40)and(d>=40)and(e>=40)):
#Grades
#Nested if
    if(avg>=80):
        print("You have Passed with Distinction")
    elif(avg>=60):
        print("You have Passed with First Class")
    elif(avg>=50):
        print("You have Passed with Second Class")
    elif(avg>=40):
        print("You have Passed with Third Class")
    else:
        print("You have Failed")
else:
    print("You have Failed")
