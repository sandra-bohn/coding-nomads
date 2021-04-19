'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''
# Define an empty Movie class.
class Movie:
    pass

# Add a dunder init method that takes two arguments "year" and "title"
class Movie:
    def __init__(self, year, title):
        self.year = year
        self.title = title

# Create a sub-class called "RomCom" that inherits from the Movie class
class RomCom(Movie):
    pass

# Create another sub-class of the Movie class called "ActionMovie"
#    that overwrites the dunder init method of Movie and adds another
#    instance variable called "pg" that is set by default to the number 13.
class ActionMovie(Movie):
    def __init__(self, year, title, pg=13):
        super().__init__(year, title)
        self.pg = pg

r = RomCom(2023, "When Vladi Met Donny")
print(r.year, r.title)

a = ActionMovie(2022, "Attack of the Cheese Balls")
print(a.year, a.title, a.pg)

# EXTRA: If you finish early, use the time to practice flushing out these
#    classes and white-boarding code. What attributes could a Movie class
#    contain? What methods? What tricks can you use through inheritance?
#    Any class attributes you could add?
class Movie:
    def __init__(self, year, title):
        self.year = year
        self.title = title
    def __str__(self):
        f"Coming in {self.year}, '{self.title}'!"

class ActionMovie(Movie):
    def __init__(self, year, title, pg=13):
        super().__init__(year, title)
        self.pg = pg
    def __str__(self):
        f"Coming in {self.year}, '{self.title}', rated {self.pg}!"
