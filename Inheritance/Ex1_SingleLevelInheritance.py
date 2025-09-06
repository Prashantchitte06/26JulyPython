
#Ex1: Single Level Inheritance

class Father:                #Super/Parent/Base class
    def car(self):
        print("method car is running from father class")

    def money(self):
        print("method money is running from father class")

    def home(self):
        print("method home is running from father class")


class Son(Father):       #Sub/child class
    def mobile(self):
        print("method mobile is running from Son class")

    # def car(self):
    #     print("method car is running from father class")
    #
    # def money(self):
    #     print("method money is running from father class")
    #
    # def home(self):
    #     print("method home is running from father class")


s1=Son()
s1.mobile()
s1.car()
s1.money()
s1.home()
