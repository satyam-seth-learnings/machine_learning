# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self,r):
        self.radius=r
    
    def area(self):
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius

c1=Circle(10)
print(f'Radius: {c1.radius}')
print(f'Area: {c1.area()}')
print(f'Perimeter: {c1.perimeter()}')