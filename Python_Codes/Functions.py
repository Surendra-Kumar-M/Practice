#add function with parameter and with return type
def add(a,b):
    return a+b
#sub function with no parameter and no return
def sub():
    print(5-3)
#mul function with parameter and no return 
def mul(a,b):
    print(a*b)
#div function no parameter with return
def div():
    return (4/2)
m=int(input("Enter the Number : "))
n=int(input("Enter the Number : "))
c=add(m,n)
d=mul(m,n)
print(c,d)
print(sub(),div())
