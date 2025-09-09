# Ex3: Variable Overriding

# Ex3.1: print only override child class variable
class parent:
   name="amol"

class child(parent):
   name="AMOL"

   def m1(self):
      print(self.name)

c=child()
print(c.name)    #AMOL
c.m1()

print("--------------------------")

# Ex3.2: print both parent & child class variable
class parent1:
   name="mahesh"

class child1(parent1):
   name="MAHESH"

   def m2(self):
       print(super().name)


c=child1()
print(c.name)      #MAHESH
c.m2()             #mahesh
