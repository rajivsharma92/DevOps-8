class Shape:

    def __init__(self, width, height):
        
        self.width = width
        
        self.height = height

    def area(self):
        
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height):
        
        super().__init__(width, height)

    def area(self):

        return self.width * self.height
    
class Circle(Shape):

    def __init__(self, radius):
        
        self.radius = radius

    def area(self):

         return 3.14159 * (self.radius ** 2)
    

rectangle1 = Rectangle(12,12)

print(f"Area of Rectangle is {rectangle1.area()}")

circle1 = Circle(3)

print(f"Area of a circle is {circle1.area()}")
