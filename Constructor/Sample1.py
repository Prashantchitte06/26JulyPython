
print("-------#Ex1- Constructor without parameter------")

class demo1:

    #without/zero parameter constructor
    #use 1: initialize object -> copy all members of class into object
    def __init__(self):                                         #constructor declaration
            print("Running without parameter constructor")      #constructor body

    def m1(self):
        print("Running method m1")

d1=demo1()       #Object creation -> constructor call ->initialize object -> copy all members of class into object
d1.m1()


print("----------------# Ex2.1: Constructor With Parameter---------------------")

class Demo2:

   def __init__(self,name):             #With parameter
       print("With Para Constructor is running- ",name)
       self.name=name                     #converting local variable info into class variable

   def m1(self):
       print("Running method m1")
       print(self.name)

d2=Demo2("amol")
d2.m1()



print("----------------# Ex2.2: Constructor With Parameter---------------------")

class Employee:

    num1=10

    def __init__(self,name,id,salary):         #with 3 para constructor
        self.name=name          #assign local variable info into class variable
        self.id=id
        self.sal=salary

    def empInfo(self):
        print(self.name)
        print(self.id)
        print(self.sal)
        print(self.num1)

e1=Employee("Amol",123,50000.1)
e1.empInfo()

print("--")
e2=Employee("Rahul",102,682682.1)
e2.empInfo()


print("----------------# Ex2.3: Constructor With Parameter---------------------")

class ArithmaticOperation:

    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def add(self):
        print("Addition-",(self.num1+self.num2))

    def mult(self):
        print("multiplication-",(self.num1*self.num2))

    def sub(self):
        print("subtraction-",(self.num1-self.num2))

s1=ArithmaticOperation(10,20)
s1.add()
s1.mult()
s1.sub()
print("--")
s2=ArithmaticOperation(5,6)
s2.add()
s2.mult()
s2.sub()



