class Marksheet():
    def Result(self,a,b,c,d,e):
        if((a>=40)and(b>=40)and(c>=40)and(d>=40)and(e>=40)):
            return "Pass"
        else:
            return "Fail"
    def Grade(self):
        if(self.Result(a,b,c,d,e)=="Pass"):
            avg=(a+b+c+d+e)/5
            if(avg>=80):
                return "Destinction"
            elif(avg>=60):
                return "First Class"
            elif(avg>=50):
                return "Second Class"
            elif(avg>=40):
                return "Third Class"
        else:
            return "RA"

N=input("Enter the Name of the Student      : ")
C=input("Enter the Class of the Student     : ")
a=int(input("Enter the mark in English          : "))
b=int(input("Enter the mark in Tamil            : "))
c=int(input("Enter the mark in Maths            : "))
d=int(input("Enter the mark in Science          : "))
e=int(input("Enter the mark in Social Science   : "))


M=Marksheet()
M.Grade()
S=["English","Tamil","Maths","Science","Social Science"]

print("-----------------------------------------------------------------")
print("|\t\t\tMarkSheet\t\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\t\tSri Ranganathar College\t\t\t\t|\n|\t\t\tResult\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\tName of the Student : ",N,"\t\t\t\t|")
print("|\t\t\t\t\t\t\t\t|\n|\tClass               : ",C,"\t\t\t\t|")
print("|\t\t\t\t\t\t\t\t|\n|\t\tSubjects\t\tMarks\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\t\t",S[0],"\t\t ",a,"\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\t\t",S[1],"\t\t\t ",b,"\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\t\t",S[2],"\t\t\t ",c,"\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\t\t",S[3],"\t\t ",d,"\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\t\t",S[4],"\t ",e,"\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("|\tRESULT:\t",M.Result(a,b,c,d,e),"\t\t\t\t\t\t|")
print("|\t\t\t\t\t\t\t\t|\n|\tGrade:\t",M.Grade(),"\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t|")
print("-----------------------------------------------------------------")
