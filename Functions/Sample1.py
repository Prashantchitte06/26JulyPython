#Ex1: Function without parameter
from importlib.util import source_hash

def f1():                #function declaration -> defKeyword functionName
    print("Hi")         #function body
    print("Hello")
    print("GM")

f1()                    #function Call  ->functionalName()
f1()    #reuse

print("----")
def add():
    num1=50
    num2=60
    print(num1+num2)

add()

print("----------------------------------")

#Ex2: Function with parameter

#Ex2.1  function with int,int(2 int) parameter
def add(num1,num2):       # num1=50, num2=60 #function with 2 int parameter
    print(num1+num2)

add(10,20)
add(50,60)
add(50,60)

print("----")
#Ex2.2  function with String parameter
def studentFullName(FN, LN):
    print("Student Full Name: ",FN,LN)

studentFullName("abc1","xyz1")
studentFullName("abc2","xyz2")


print("----")
#Ex2.2  function with all types of parameter
def studentDetails(name,rollNum,per, grade):
    print("Student Name: ",name)
    print("Student rollNum: ", rollNum)
    print("Student percentage: ", per,"%")
    print("Student grade: ", grade)

studentDetails("abc1",101,65.5,"A+")
studentDetails("abc2",102,55.4,"A")






