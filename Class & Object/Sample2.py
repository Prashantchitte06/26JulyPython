# Ex2: static methods

class Demo2:
    @staticmethod         #static method
    def m3():
        print("Running static method m3")

    @staticmethod      #static method
    def add(num1,num2):
        print(num1+num2)

#To call static method
# className.methodName()

Demo2.m3()
Demo2.add(10,15)