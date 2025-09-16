#ModuleName2:  Operations

#Approach1
import Calculator

#call functions
Calculator.add(10,20)
Calculator.mul(10,20)


#call class/ methods from class
obj1=Calculator.Demo1()
obj1.m1()
obj1.m2()

print("-------------------")

#Approach2.1   -> import only specific function/classes
from Calculator import add,Demo1
add(10,20)

obj2=Demo1()
obj2.m1()
obj2.m2()

print("-------")

#Approach2.2              -> import all specific function/classes
from Calculator import *
add(10,20)
mul(10,20)

obj2=Demo1()
obj2.m1()
obj2.m2()

