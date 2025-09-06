
a,b=10,20     #global variable

class Sample4:

  a,b=30,40      #class variable

  def add(self,a,b):        #local variable
      print(a+b)                  #50+60
      print(self.a+self.b)        #30+40
      print(globals()['a']+globals()['b'])   #10+20

s4=Sample4()
s4.add(50,60)
