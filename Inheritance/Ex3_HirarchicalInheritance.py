#Ex3: Hierarchical Inheritance

class Father:                #Super class
    def car(self):
        print("method car is running from father class")

    def money(self):
        print("method money is running from father class")

    def home(self):
        print("method home is running from father class")


class Son1(Father):       #Sub1 class
    def mobile(self):
        print("method mobile is running from Son1 class")

class Son2(Father):       #Sub1 class
    def laptop(self):
        print("method laptop is running from Son2 class")


print("----Features of Son1---")
s1=Son1()
s1.mobile()
s1.car()
s1.money()
s1.home()

print("----Features of Son2---")
s2=Son2()
s2.laptop()
s2.car()
s2.money()
s2.home()