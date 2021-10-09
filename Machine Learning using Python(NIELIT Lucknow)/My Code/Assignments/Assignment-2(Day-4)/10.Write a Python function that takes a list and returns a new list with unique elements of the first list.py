# Write a Python function that takes a list and returns a new list with unique elements of the first list. 

def unique(l):
    return list(set(l))

l=[10,45,41,48,75,74,41,74,14,54]
print(unique(l))