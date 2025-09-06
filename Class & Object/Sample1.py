
#Ex1: Instance/non-static method

class Demo1:
    def m1(self):                  #Without/Zero
        print("Running method m1")

    def findSquareOfNum(self,num):  #With parameter
        print(num*num)

    def m2(self):                    #Method with no implementation
        pass


#to call instance method
#1: create object/instance of class  -> className() -> constructor call -> use to copy all the members of class into object
#2: call method -> objName.methodName()

d1=Demo1()
d1.m1()
d1.findSquareOfNum(5)
d1.m2()



