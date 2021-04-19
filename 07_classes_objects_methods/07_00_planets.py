'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    "Stores planet information"
    def __init__(self, name, color, size, order):
        "Defines attributes of planet"
        self.name = name
        self.color = color
        self.size = size
        self.order = order
    def __str__(self):
        "Prints description of planet"
        return f"The planet {self.name} is a {self.size}, {self.color} planet that is {self.order} from the sun."

earth = Planet('Earth', 'blue', 'medium', 'third')
print(earth)