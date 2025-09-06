num1=10       #global variable

class Demo1:

   num2=20     #class variable

   @staticmethod
   def m1():
       num3=30              #local variable
       print(num3)        #30
       print(Demo1.num2)   #20      #className.classVariableName
       print(num1)


Demo1.m1()
