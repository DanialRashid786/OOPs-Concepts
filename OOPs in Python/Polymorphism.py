class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Polymorphic behavior with different objects of Shape class
rectangle = Rectangle(5, 10)
circle = Circle(7)

print(rectangle.area())    # Output: 50
print(circle.area())       # Output: 153.86
