#key-int, value-Str
dict2={1:"mahesh",2:200,3:55.6}
print(dict2)

#key-int, value-Str
dict1={1:"mahesh",2:"ganesh",3:"ramesh"}
print(dict1)

print("------get length of dict-------")
print(len(dict1))   #3

print("------get value of specific key------")
print(dict1[2])

print("-----Add new k-v pair-----")
dict1[4]="rahul"
print(dict1)

print("-----update/modify value existing key-----")
dict1[1]="MAHESH"
print(dict1)

print("-----Remove any k-v pair-----")
dict1.pop(3)
print(dict1)

print("-----Remove last inserted item(k-v)-----")
dict1.popitem()
print(dict1)

print("-----check if key exist-----")
print(1 in dict1)         #True
print(5 in dict1)         #False


print("-----get all keys-----")
print(dict1.keys())
for key in dict1.keys():
    print(key)

print("-----get all values-----")
print(dict1.values())
for value in dict1.values():
    print(value)

print("-----get all keys-values(items)-----")
print(dict1.items())
for key,value in dict1.items():
    print(key, value)

















