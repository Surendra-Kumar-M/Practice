#Class Creation
class oops():
    a=10
    b=20
    def add(self):
        c=self.a+self.b
        return(c)

A=oops()    #Object Creation Objrct_name=Class_name() //a=class1()
print(A.add())   #Method calling Object_name.Method_name() //a.method1()


class Area():
    a=int(input("Enter the Side of the square"))
    def Sq(self):
        ar=self.a**2
        return(ar)
B=Area()
print(B.Sq())


