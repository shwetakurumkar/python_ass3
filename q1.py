import math

class Circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.area()}")
print(f"Circumference of the circle: {circle.circumference()}")