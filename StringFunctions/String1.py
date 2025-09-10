s1="velocity"
s2="ABCD"
s3="abcd"

print(len(s1))      #8

print(s1.upper())
# s1=s1.upper()       #Reinitialization
# print(s1)

print(s2.lower())
# s2=s2.lower()
# print(s2)

print("------")
print(s2==s3)                   #compare data & case
print(s2.__eq__(s3))            #compare data & case
print(s2.lower()==s3.lower())   #compare only data
print("------")

print("ve" in s1)
print(s1.__contains__("ve"))
print(s1.startswith("ve"))
print(s1.endswith("ty"))



