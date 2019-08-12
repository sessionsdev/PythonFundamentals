'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Vehicle:
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed

class Motorcycle(Vehicle):
    def __init__(self, color, max_speed, model):
        super().__init__(color, max_speed)
        self.model = model

class Harley(Motorcycle):
    def __init__(self, color, max_speed, model, style):
        super().__init__(color, max_speed, model)
        self.style = style


bike = Harley("black", 75, "harley", "Chopper")

print(bike.color)