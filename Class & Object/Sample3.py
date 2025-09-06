# Ex3: Static & non-static method in same class

class Demo3:
    def m1(self):
        print("Running instance method-m1")

    def m2(self):
        print("Running instance method-m2")

    @staticmethod
    def m3():
        print("Running static method-m3")

    @staticmethod
    def m4():
        print("Running static method-m4")


#call instance/non-static method
d3=Demo3()
d3.m1()
d3.m2()

#call static method
Demo3.m3()
Demo3.m4()