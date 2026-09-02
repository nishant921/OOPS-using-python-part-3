class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def get_info(self):
        print(self.name,self.gender,'\n',self.address.house(),self.address.city,self.address.pin,self.address.state)

    # HOW TO USE METHODS IN AGGREGATION
    def edit_profile(self,edit_name,new_house_no,new_city,new_pincode,new_state):
        self.name = edit_name
        self.address.edit_address(new_house_no,new_city,new_pincode,new_state)
    

class Address:
    def __init__(self,house_no,city,pin,state):
        self.__house_no = house_no
        self.city = city
        self.pin = pin
        self.state = state

    # getter
    def house(self):
        return self.__house_no

    # HOW TO USE METHODS IN AGGREGATION
    def edit_address(self,new_house_no,new_city,new_pincode,new_state):
        self.__house_no = new_house_no
        self.city = new_city
        self.pin = new_pincode
        self.state = new_state


add1=Address('1-c','New Delhi',110090,'Delhi')
cust=Customer('Nishant','M',add1)
cust.get_info()

# add1.edit_address()
cust.edit_profile('nish','111-p','gorakhpur',24590,'UP')
cust.get_info()