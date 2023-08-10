#Arithmetic Operations
a=lambda n1,n2:n1+n2
s=lambda n1,n2:n1-n2
m=lambda n1,n2:n1*n2
d=lambda n1,n2:n1/n2
M=lambda n1,n2:n1%n2
f=lambda n1,n2:n1//n2

#Bitwise Operations
ab=lambda n1,n2:n1&n2
ob=lambda n1,n2:n1|n2
nb=lambda n1:~n1
lsb=lambda n1:n1<<1
rsb=lambda n1:n1>>2
exb=lambda n1,n2:n1^n2

#Logical Operation
al=lambda n1,n2:n1>n2 and n1<n2
ol=lambda n1,n2:n1>n2 or n1<n2
nl=lambda n1,n2:not(n1>n2)

n1=int(input("Enter the Number : "))
n2=int(input("Enter the Number : "))
print("\n\t\tArithmetic Operations\n")
print("Sum of ",n1," and ",n2," is ",a(n1,n2))
print("Subtraction of ",n1," and ",n2," is ",s(n1,n2))
print("Multiplication of ",n1," and ",n2," is ",m(n1,n2))
print("Division of ",n1," and ",n2," is ",d(n1,n2))
print("Modulus of ",n1," and ",n2," is ",M(n1,n2))
print("Floor Division of ",n1," and ",n2," is ",f(n1,n2))

print("\n\t\tBitwise Operations\n")
print("AND of ",n1," and ",n2," is ",ab(n1,n2))
print("OR of ",n1," and ",n2," is ",ob(n1,n2))
print("NOT of ",n1," is ",nb(n1))
print("EX-OR of ",n1," and ",n2," is ",exb(n1,n2))
print("Left Shift of ",n1," by 1 is ",lsb(n1))
print("Right Shift of ",n1," by 2 is ",rsb(n1))

print("\n\t\tLogical Operations\n")
print("Logical AND of ",n1," and ",n2," is ",al(n1,n2))
print("Logical OR of ",n1," and ",n2," is ",ol(n1,n2))
print("Logical NOT of ",n1," is ",nl(n1,n2))




