# Calculate average of sum of cube of all numbers of a list by using lambda and map. Use len function to calculate the length of the list.

l=[1,2,3,4,5,6,7,8,9,10]
cubes=list(map(lambda x: x**3,l))
print(sum(cubes)/len(l))