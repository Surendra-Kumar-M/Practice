#Getting inputs
a=int(input("Enter the mark in English"))
b=int(input("Enter the mark in Tamil"))
c=int(input("Enter the mark in Maths"))
d=int(input("Enter the mark in Science"))
e=int(input("Enter the mark in Social"))
#Calculation
#Ladder if
if(a>=40):
    if(b>=40):
        if(c>=40):
            if(d>=40):
                if(e>=40):
                    print("The Student is Pass")
                else:
                    print("The Student is Fail")
            else:
                print("The Student is Fail")
        else:
            print("The Student is Fail")
    else:
        print("The Student is Fail")
else:
    print("The Student is Fail")
