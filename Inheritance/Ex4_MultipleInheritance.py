#4: Example of multiple inheritance

class A:            #Super class1
   def m1(self):
       print("Method m1 from A class")


class B:          #Super class2
   def m2(self):
       print("Method m2 from B class")


class C(A,B):     #Sub class
   def m3(self):
       print("Method m3 from C class")


print("------Features of class C-----")
c=C()
c.m1()
c.m2()
c.m3()
