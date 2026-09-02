class User:
    def __init__(self):
        self.name ='nishant'

    def get_login(self):
        print('login')

class Student(User):
    def __init__(self):
        self.roll=23

    def enroll(self):
        print("Enrolled in the course")

u = User()
s = Student()
# print(s.name)
print(s.roll)
s.get_login()
s.enroll()