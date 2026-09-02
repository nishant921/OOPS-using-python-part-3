class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("BUY PHONE")

class SmartPhone(Phone):
    
    def buy(self):
        print("BUY SMARTPHONE")
        # super() to access base class method or constructor
        super().buy()

s= SmartPhone(20000,'moto',12)
s.buy()


class Car:
    def move(self):
        return "Drive on roads! 🚗"

class Boat:
    def move(self):
        return "Sail on water! ⛵"

# A unified interface executing different actions
for vehicle in [Car(), Boat()]:
    print(vehicle.move())

