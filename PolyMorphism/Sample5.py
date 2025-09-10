# Example1: Method overloading

class Demo:

   def add(self,a=0, b=0, c=0, d=0):
       print(a+b+c+d)

d=Demo()
d.add(10,20)    #30
d.add(10,20,30) #60
d.add(10,20,30,40)


print("-----------")

class Sample:
   def printName(self,sName="xyz"):
       print(sName)

s=Sample()
s.printName()
s.printName("Mahesh")


print("----------------")

print(5+5)
print("5"+"5")