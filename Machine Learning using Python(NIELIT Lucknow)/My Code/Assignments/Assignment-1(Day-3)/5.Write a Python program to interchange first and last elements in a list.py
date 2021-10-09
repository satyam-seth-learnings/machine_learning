# Write a Python program to interchange first and last elements in a list.

# Logic-1

l=[1,2,3,4,5]
print(f'List: {l}')
l[0],l[-1]=l[-1],l[0]
print(f'List: {l}')

# Logic-2

# l=[1,2,3,4,5]
# print(f'List: {l}')
# l.insert(0,l.pop())
# l.append(l.pop(1))
# print(f'List: {l}')