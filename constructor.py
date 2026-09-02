# Constructor inherited by child class

class Phone:
    def __init__(self):
        print("Inside Phone Constructor")


class Smartphone(Phone):
    pass

s=Smartphone()

# same example
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a smartphone")

class Smartphone(Phone):
    pass

s=Smartphone(29900,'moto',12)
s.buy()

# BOTH CHILD AND PARENT CONSTRUCTOR
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a smartphone")

class Smartphone(Phone):
    def __init__(self,os,ram):
        print("Inside child/smartphone class")
        self.os = os
        self.ram = ram

s=Smartphone('ios',12)
s.buy()
