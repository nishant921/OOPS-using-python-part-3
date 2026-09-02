# using super() in Constructor 
class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("BUY Phone")
    def get_price(self):
        return self.__price

    
class SmartPhone(Phone):
    def __init__(self, price, brand, camera,os,ram):
        print("right now smartphone constructor")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("right now smartphone constructor")

    def buy(self):
        print("BUY SmartPhone")

s = SmartPhone(20000,'moto',12,'android',8)
s.buy()
print(s.brand)
print(s.os)
print(s.camera)
print(s.get_price())
# print(s._Phone__price) we should not do it