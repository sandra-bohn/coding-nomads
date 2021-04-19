'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class Pet():
    def __init__(self, name, breed, sex, age, species):
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


class Dog(Pet):
    def __init__(self, name, breed, sex, age, species='canine'):
        super().__init__(name, breed, sex, age, species)


class Cat(Pet):
    def __init__(self, name, breed, sex, age, species='feline'):
        super().__init__(name, breed, sex, age, species)


class Puppy(Dog):
    def __init__(self, name, breed, sex, age=0, species='canine'):
        super().__init__(name, breed, sex, age, species)

class SkiMountain(Mountain):
    def __init__(self, name, height, range, difficulty):
        super().__init__(name, height, range)
        self.difficulty = difficulty
    def __str__(self):
        "describes mountain"
        return f"{self.name} is a {self.height} ft mountain in the {self.range} range with {self.difficulty} ski trails."

spot = Pet('Spot', 'mixed', 'male', 4, 'canine')
print(spot)
smalls = Dog('Smalls', 'beagle', 'female', 2)
print(smalls)
tiny = Puppy('Tiny', 'labrador', 'male')
print(tiny)

frosty = SkiMountain('Mt Frosty', 3200, 'Snowy Mountains', 'easy')
print(frosty)