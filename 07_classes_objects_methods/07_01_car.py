'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():
    def __init__(self, name, model, year, max_speed):
        "Assigns car's name, model, year, and max_speed"
        self.name = name
        self.model = model
        self.year = year
        self.max_speed = max_speed
    def __str__(self):
        return f"{self.name} is a {self.year} {self.model} with a maximum speed of {self.max_speed}."
    def increase_max(self):
        "Increases max_speed by 5 each time it is called"
        self.max_speed += 5

mycar = Car('My car', 'Honda Fit', 2013, 100)
oldcar = Car('My old car', 'Toyota Celica', 2001, 110)
print(mycar)
mycar.increase_max()
print(mycar)
print(oldcar)
oldcar.increase_max()
oldcar.increase_max()
print(oldcar)