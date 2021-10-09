# Write a Python program to swap two numbers and print.

# Logic-1

num1=int(input('Enter 1st number :'))
num2=int(input('Enter 2nd number :'))
temp=num1
num1=num2
num2=temp
print(f'First number {num1}')
print(f'Second number {num2}')

# Logic-2

# num1,num2=map(int,input('Enter two numbers separated by space: ').split())
# print(f'Value of first number: {num1}')
# print(f'Value of second number: {num2}')
# num1,num2=num2,num1
# print(f'Value of first number: {num1}')
# print(f'Value of second number: {num2}')