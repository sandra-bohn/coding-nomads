'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
fishy_fish = [i for i in fish_tuple if i.find('fish') > -1]
print(fishy_fish)
