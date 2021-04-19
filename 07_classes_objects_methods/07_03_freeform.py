'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
class Pet():
    def __init__(self, name, species, breed, age, sex):
        "defines pet of any species or breed"
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.sex = sex
    def __str__(self):
        "describes pet"
        return f"{self.name} is a {self.sex}, {self.age}-year-old {self.breed} {self.species}."
    def __add__(self, other):
        "allows user to add to the pet's age"
        print(f"adding {other} to {self.age}")
        return Pet(self.age + other)

class Tree():
    def __init__(self, id, species, height, diameter):
        "defines a tree by species and size"
        self.id = id
        self.species = species
        self.height = height
        self.diameter = diameter
    def __str__(self):
        "describes tree"
        return f"Tree {self.id} is a {self.height} ft tall, {self.diameter} in wide {self.species}."

class Mountain():
    def __init__(self, name, height, range):
        "defines mountain by height and location"
        self.name = name
        self.height = height
        self.range = range
    def __str__(self):
        "describes mountain"
        return f"{self.name} is a {self.height} ft mountain in the {self.range} mountain range."

spot = Pet('Spot', 'canine', 'mixed', 4, 'male')
fluffy = Pet('Fluffy', 'feline', 'Persian', 2, 'female')
t123 = Tree(123, 'pine', 142, 33)
t456 = Tree(456, 'fir', 108, 29)
mtchoc = Mountain('Mt Chocolate', 6800, 'Yummy Mountains')
mtbutt = Mountain('Mt Butterscotch', 5900, 'Yummy Mountains')

print(spot)
# add a year to Spot's age
spot.age += 1
print(spot)
print(fluffy)
# add 2 years to Fluffy's age
fluffy.age += 2
print(fluffy)
print(t123)
print(t456)
print(mtchoc, mtbutt)