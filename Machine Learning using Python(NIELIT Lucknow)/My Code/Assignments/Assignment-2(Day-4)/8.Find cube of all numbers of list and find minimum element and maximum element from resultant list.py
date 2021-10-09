# Using lambda and map calculate the cube of all numbers of a list and find minimum element and maximum element from the resultant list.

l=[1,2,6,4,8,9,10]
cubes=list(map(lambda x: x**3,l))
print(f'Cube of all numbers: {cubes}')
print(f'Minimum element: {min(cubes)}')
print(f'Maximum element: {max(cubes)}')