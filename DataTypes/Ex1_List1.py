
ls=["Amol",101,65.5,"A+",101]

#print type of object/variable
print(type(ls))

#display data
print(ls)

#get size of list
print(len(ls))

#get specific data from list
print(ls[0])        #Amol
print(ls[1])        #101

#Add data in list append/insert/extend
#Add new element at last position
ls.append("xyz")
print(ls)

#add new element at specific position/ add element in between list -> right shift operation
ls.insert(0,200)
print(ls)

#add multiple new elements at the end
ls.extend([10,40,"abc",55.5])
print(ls)


#remove data from list -> pop(), pop(index), remove(object/element)
#remove element from last position
ls.pop()
print(ls)

#remove data from specific index
ls.pop(2)
print(ls)

#remove specific element
ls.remove("A+")
print(ls)


#copy list
ls1=ls.copy()
print(ls1)

print("------print all data using for loop------")
for i in ls:
    print(i)

print("---print specific data using for loop---")
for i in range(0,4):   # 0 to 3+1
    print(ls[i])







