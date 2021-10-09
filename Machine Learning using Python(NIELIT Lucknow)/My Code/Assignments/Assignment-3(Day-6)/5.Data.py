# Write a Python program to create the class named data that has three members – id, name and basic_salary. Create a new class named calculation that inherits the class data and calculates the HRA, DA and Gross salary using function. Display the id, name, salary, HRA, DA and gross salary. HRA is 45% of basis salary and DA is 60% of basic salary. Input the values from the user.

class Data:
    def __init__(self,e_id,name,basic_salary):
        self.e_id=e_id
        self.name=name
        self.basic_salary=basic_salary

class Calculation(Data):
    def cal(self):
        hrd=(self.basic_salary*45)/100
        da=(self.basic_salary*60)/100
        gross_salary=self.basic_salary+hrd+da

        print('ID:',self.e_id)
        print('Name:',self.name)
        print('Salary:',self.basic_salary)
        print('HRA:',hrd)
        print('DA:',da)
        print('Gross Salary:',gross_salary)

e_id=input('Enter the ID:')
name=input('Enetr the Name:')
salary=int(input('Enter Basic Salary:'))

c1=Calculation(e_id,name,salary)
c1.cal()