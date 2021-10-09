# Write a Python function to print area and perimeter of a circle.

def circle(r):
    area=3.14*(r**2)
    perimeter=2*3.14*r
    print('Area of circle:',area)
    print('Perimeter of circle:',perimeter)

circle(int(input()))