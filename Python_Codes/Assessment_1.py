def students(n,a,*marks):
    print("Name of the Student :",n)
    print("Age of the Student",a)
    print("Marks of the Student")
    if(len(marks[0])<=5):
        for i in range((6-len(marks[0]))):
            marks[0].append(0)
    i=0
    while(i<5 and len(marks[0])>=5):
        print("Subject",i+1,' : ',marks[0][i])
        i+=1

        
j=0
while (j<10):
    n=input("Enter the Name of the Student : ")
    a=int(input("Enter the Age of the Student : "))
    m=input("Enter Marks : ").split(',')
    students(n,a,m)
    j+=1
