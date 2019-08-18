'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

class Beer:
    def __init__(self, style = "IPA", abv = 5, origin = "California"):
        self.style = style
        self.abv = abv
        self.origin = origin

    def __str__(self):
        return (f"This beer is an {self.style} with an ABV of {self.abv}% from {self.origin}")

    def __add__(self, other):
        abv1 = self.abv
        abv2 = other.abv
        return abv1 + abv2



class Dog:
    def __init__(self, breed = "Poodle", weight = 35, color = "White"):
        self.breed = breed
        self.weight = weight
        self.color = color

    def __str__(self):
        return (f"This dog is a {self.color} {self.breed} and it weighs {self.weight} lbs!")



class Drill:
    def __init__(self, diameter = 1, length = 12, material = "Concrete", machine = "SDS+"):
        self.diameter = diameter
        self.length = length
        self.material = material
        self.machine = machine

    def __str__(self):
        return (f"This is a {self.diameter} by {self.length} drill for {self.material}.  Use a {self.machine} machine!")


beer1 = Beer('IPA', 35, 'New York')
beer2 = Beer('Lager', 10, 'Califonia')

print(beer1 + beer2)