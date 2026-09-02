class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("BUY PHONE")

class SmartPhone(Phone):
    # method overriding
    def buy(self):
        print("BUY SMARTPHONE")

s= SmartPhone(20000,'moto',12)
s.buy()