import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter")

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.diameter
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return (f"Circle with radius {self.radius}, "
                f"diameter {self.diameter}, "
                f"area {self.area:.2f}")
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented
    
    def __lt__(self, other):   # less than
        if isinstance(other, Circle):
            return self.area < other.area   # compare by area
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius  # or use self.area == other.area
        return NotImplemented

    def __gt__(self, other):   # greater than
        return self.area > other.area
    
c1 = Circle(radius=5)
c2 = Circle(radius=2)
c3 = Circle(diameter=10)   # radius 5
c4 = Circle(radius=7)

circles = [c1, c2, c3, c4]
    
circles.sort()   # sorts in place using __lt__

# Print sorted circles
for c in circles:
    print(c)


import turtle

radii = [2, 5, 5, 7]

screen = turtle.Screen()
screen.title("Sorted Circles")

t = turtle.Turtle()
t.speed(1)

t.penup()
t.goto(-200, 0) 
t.pendown()

for r in radii:
    t.circle(r * 10)  # scale radius for visibility
    t.penup()
    t.forward(r * 20 + 20)  # move right for next circle
    t.pendown()

turtle.done()

sorted_circles = sorted(circles)

# Draw sorted circles
for c in sorted_circles:
    t.circle(c.radius * 10)  # scale factor
    t.penup()
    t.forward(c.radius * 20 + 20)
    t.pendown()





