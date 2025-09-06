num=50          #global variable   scope -> through the class

def m1():
    num1=10         #local variable  -> scope -> within function only
    print(num1)    #10
    print(num)     #50

def m2():
    num2=20
    print(num2)      #20
    #print(num1)
    print(num)         #50

def m3():
    num3=30
    print(num3)         #30
     #print(num2)
    print(num)          #50

m1()
m2()
m3()
