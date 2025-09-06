
#Create Set
s1= {"Amol",101,65.5,"A+",101}

print(s1)

#Accessing single data using index -> not possible
# print(s1[0])

#get size of set
print(len(s1))

print("---------Adding elements-------")
#Add single elements
s1.add("Electrical")
print(s1)

#Add multiple elements
s1.update([500,600])
print(s1)


print("---------Removing Elements-----------")
s1.remove(500)
print(s1)

s1.discard(100)
print(s1)

# s1.pop()
# print(s1)

print("------copy set------")
s2=s1.copy()
print(s2)


print("-----Sorting------")
s3={50,30,20,40,10}
s3=sorted(s3)
print(s3)


print("------clear set------")
s3.clear()
print(s3)

print("------delete set------")
del s3
# print(s3)

print("------Convert Set to list----")
s4={50,30,20,40,10}
print(type(s4))

s5=list(s4)                  #  convert set to list
print(type(s5))
print(s5)
print(s5[0])

print("------reverse operation----")
s5.reverse()
print(s5)





