# Write a python program to delete an object's properties

class Student:
    def __init__(self,roll,name,age):
        self.roll=roll
        self.name=name
        self.age=age

s1=Student(101,'Satyam',20)
print(s1.roll)
print(s1.name)
print(s1.age)
delattr(s1,'age')
# print(s1.age)   AttributeError: 'Student' object has no attribute 'age'
del s1.name
# print(s1.name)  AttributeError: 'Student' object has no attribute 'name'
