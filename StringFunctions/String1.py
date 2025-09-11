s1="velocity"
s2="ABCD"
s3="abcd"
s4="abcdabcaba"
s5=" abcd "
s6="my name is abc"

s7="  "
s8="abcd"
s9="1223"
s10="abc123"

print(s10.isalnum())
print(s9.isdigit())
print(s8.isalpha())
print(s7.isspace())
print(s6.count("my"))   #1

#convert 1st to upper case
print(s3.capitalize())
#convert 1st letter of each word to upper case
print(s6.title())

#split statement
ls=s6.split(" ")     #[my    name    is abc]
print(ls)

#remove spaces from string
print(s5)
print(s5.strip())
#remove space from left
print(s5.lstrip())
#remove space from right
print(s5.rstrip())

#CONCAT 2 STRINGS
print(s2+s3)

print("-----------")
#find index of specific char
print(s4.index("b"))
print(s4.find("b"))

#find index of specific char from right side (last occurance of char)
print(s4.rfind("b"))   #8


#find char using index
print(s1[3])
#Substring
print(s1[3:])
print(s1[3:6])      #3-5

print("-------------")
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



