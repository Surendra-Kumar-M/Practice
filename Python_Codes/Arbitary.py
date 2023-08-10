#Arbitary Arguments
def Samp(*a):
    print(a[-1])

Samp(1,2,3,4,5)

#Keyword Arguments
def Kumar(name):
    return (name+' Kumar')
n=input("Enter Name ")
print(Kumar(name=n))

#KW Arguments
def a(**kids):
    print(kids['lname']) #key name should be in Quotes
a(fname="SK",lname="Tamil",surname="Sri")
 

