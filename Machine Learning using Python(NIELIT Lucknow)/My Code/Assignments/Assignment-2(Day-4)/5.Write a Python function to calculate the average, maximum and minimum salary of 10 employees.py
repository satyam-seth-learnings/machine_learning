# Write a Python function to calculate the average, maximum and minimum salary of 10 employees.

def salary(l):
    avg=sum(l)/len(l)
    print(f'Average Salary: {avg}')
    print(f'Maximun Salary: {max(l)}')
    print(f'Minimum Salary: {min(l)}')

list_of_salary=list(map(eval,input('Enter the salary of 10 employees separated by space: ').split()))
salary(list_of_salary)