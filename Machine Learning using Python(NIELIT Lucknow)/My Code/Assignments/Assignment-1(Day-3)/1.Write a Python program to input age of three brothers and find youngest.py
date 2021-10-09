# Write a Python program to input age of three brothers and find youngest

# Logic-1

ages=[]
for i in range(3):
    ages.append(int(input(f'Enter the age of brother {i+1}:')))
print('Age of youngest brother: ',min(ages))

# Logic-2

# print(min([int(input(f'Enter the age of brother {i+1}:')) for i in range(3)]))

# Logic-3

# print(min(map(int,input().split())))