# Ex2: Example of local, global & class variable

num1=10       #global variable

class Demo1:

    num2=20     #class variable

    def m1(self):
        num3=30              #local variable
        print(num3)        #30
        print(self.num2)   #20

    def m2(self):
        num4=40                #local variable
        print(num4)           #40
        print(self.num2)     #20


d1=Demo1()
d1.m1()
d1.m2()
print(d1.num2)
