
#Sorting operation
s1=[20,50,10,40,30]
print("------Before sorting-------")
print(s1)


print("-----After sorting-> Ascending order------")
s1.sort()       #[10,20,30,40,50]
print(s1)


print("-----sort data in reverse order------")
s1.reverse()     #[50,40,30,20,10]
print(s1)

print("----------")
#Searching & Counting
s2=[1,5,2,6,7,8,0,2,8,2,1]

print(s2.index(5))   #return index of element ->1st ocurance
print(s2.count(2))   #return ocu/count of element  -> imp


print("------Clear list-----")
s2.clear()
print(s2)

print("------delete list-----")
del s2
print(s2)
