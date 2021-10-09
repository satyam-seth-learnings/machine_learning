# Write a Python program to check whether a year is leap year or not

# Logic-1

year=int(input('Enetr Year: '))
if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# Logic-2

# from calendar import isleap
# year=int(input('Enetr Year: '))
# if isleap(year):
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')