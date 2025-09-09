# Ex2: Method Overriding With Super()
#super class
class A:
   def m1(self):
       print("method m1 from parent class")

#sub class
class B(A):
   def m1(self):
       super().m1()
       print("method m1 from child class")


b=B()
b.m1()
