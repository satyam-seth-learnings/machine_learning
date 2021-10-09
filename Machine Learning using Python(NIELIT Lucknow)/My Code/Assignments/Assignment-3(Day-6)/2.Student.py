#  Write a python class to display student’s roll number, Name, marks of 3 subjects using functions. Also display sum and average of their marks using function.

class Student:
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
        
    def display(self):
        add=sum(self.marks)
        print(f'Roll No: {self.roll}')
        print(f'Name: {self.name}')
        for i,m in enumerate(self.marks):
            print(f'Marks {i+1}: {m}')
        print(f'Sum of Marks: {add}')
        print(f'Average of Marks: {add/len(self.marks)}')

s1=Student(101,'Satyam',(70,80,90))
s1.display()