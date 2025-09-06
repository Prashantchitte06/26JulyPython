# Ex1: Example of local & global variable

num1=10         #global variable

def f1():
    num2=20    #local variable
    print(num2)       #20
    print(num1)       #10

def f2():
    num3=30    #local variable
    print(num3)         #30
    print(num1)        #10

f1()
f2()
