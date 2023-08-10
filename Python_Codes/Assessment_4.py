import ARP
import LRP
import BWP

n1=int(input("Enter the Number : "))
n2=int(input("Enter the Number : "))
print("\n\t\tArithmetic Operations\n")
print("Sum of ",n1," and ",n2," is ",ARP.a(n1,n2))
print("Subtraction of ",n1," and ",n2," is ",ARP.s(n1,n2))
print("Multiplication of ",n1," and ",n2," is ",ARP.m(n1,n2))
print("Division of ",n1," and ",n2," is ",ARP.d(n1,n2))
print("Modulus of ",n1," and ",n2," is ",ARP.mo(n1,n2))
print("Floor Division of ",n1," and ",n2," is ",ARP.fd(n1,n2))

print("\n\t\tBitwise Operations\n")
print("AND of ",n1," and ",n2," is ",BWP.B_And(n1,n2))
print("OR of ",n1," and ",n2," is ",BWP.B_Or(n1,n2))
print("NOT of ",n1," is ",BWP.B_Comp(n1))
print("EX-OR of ",n1," and ",n2," is ",BWP.B_EX(n1,n2))
print("Left Shift of ",n1," by ",n2," is ",BWP.B_Sl(n1,n2))
print("Right Shift of ",n1," by ",n2," is ",BWP.B_Sr(n1,n2))

print("\n\t\tLogical Operations\n")
print("Logical AND of ",n1," and ",n2," is ",LRP.And(n1,n2))
print("Logical OR of ",n1," and ",n2," is ",LRP.Or(n1,n2))
print("Logical NOT of ",n1," is ",LRP.Not(n1,n2))
