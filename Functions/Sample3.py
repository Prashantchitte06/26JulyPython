#Ex5: positional parameter
def studentDetails(name,rollNum):
    print("My name is: ",name)
    print("My roll num is: ", rollNum)

studentDetails("rahul",101)       #correct order
studentDetails(102,"ganesh")      # incorrect order


print("-----------------")

#Ex6: default/optional parameter
def studentDetails1(name,rollNum=10):
    print("My name is: ",name)
    print("My roll num is: ", rollNum)

studentDetails1("rahul")
studentDetails1("rahul",20)

print("-----------------")

#Ex7: keyword parameter
def studentDetails2(name,rollNum):
    print("My name is: ",name)
    print("My roll num is: ", rollNum)

# studentDetails2("rahul",101)
studentDetails2(name="amol",rollNum=103)
studentDetails2(rollNum=104,name="mahesh")   #order doesn't matter
