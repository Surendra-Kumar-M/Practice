#Inheritance
class parent():
    def Father(self):
        return "Appa"
    def Mother(self):
        return "Amma"

class child(parent):
    def C1(self,a):
        return ("Child",a)

a=child()
print(a.Father())
print(a.Mother())
print(a.C1(1))
