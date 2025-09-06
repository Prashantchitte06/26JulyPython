
#1.1 function without parameter
def f1():     #function declaration
    print("Hi")        #function body
    print("Hello")
    print("GM")

f1()   #function call -> functionName()
f1()

print("---")

#1.2
def add():
    num1=10
    num2=20
    print(num1+num2)

add()
add()

print("-------------")

def add1(num1, num2):
    print(num1+num2)

add1(50,60)
add1(4 ,5)


def studentFullName(FN,LN):
    print("Firstname: ",FN)
    print("lastname: ", LN)

studentFullName("abc1","xyz1")
studentFullName("abc2","xyz2")

print("----s")
def studentDeatils(Name,rollNum,per,grade):
    print("Name: ",Name)
    print("Rollnum: ", rollNum)
    print("percentage: ", per)
    print("grade: ", grade)

studentDeatils("Amol",101,56.1,"A+")


