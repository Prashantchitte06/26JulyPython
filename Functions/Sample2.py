# function with return type

#function returns single value
def getStudentName():
    name="rahul"
    return name

s1=getStudentName()
print(s1)


def add(num1, num2):
    num3=num1+num2
    return num3

num4=add(10,20)     #30
print(num4*num4)


print("-------------")
#function returns multiple values
def getStudentDetails():
    FN="rahul"
    LN="Patil"
    return FN,LN

FNValue,LNValue=getStudentDetails()
print("Student details: ",FNValue,LNValue)


def getAddMult(num1, num2):
    add=num1+num2;
    mult=num1*num2
    return add, mult

addValue,multValue=getAddMult(5,6)
print("Addition & Multiplication of 2 num: ",addValue,"&",multValue)



