# Example1 -> method override

class GrandFather:
   def home(self):
       print("1 BHK")

   def money(self):
       print("1 Lakh")


class Father(GrandFather):
   def home(self):               #method override
       print("2 BHK")

   def money(self):
       print("2 Lakh")


class Son(Father):
   def home(self):
       print("3 BHK")

   def money(self):
       print("3 Lakh")

print("------Properties of grandfather------")
g=GrandFather()
g.home()
g.money()

print("------Properties of father------")
f=Father()
f.home()
f.money()

print("------Properties of son------")
s=Son()
s.home()
s.money()
