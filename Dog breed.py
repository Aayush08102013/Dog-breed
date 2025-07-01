class Dog():

    def __init__(self, colour, breed, facts):
        self.colour = colour
        self.breed = breed
        self.facts = facts

husky = Dog('whiteish-grey', 'husky', "Huskies are intelligent, playfull and very freindly!")
german_shepard = Dog('Brown and black', 'German Shepard', "German shepards are used as police dogs")

print( husky.colour,',', husky.breed,',', husky.facts, '\n',german_shepard.colour, ',', german_shepard.breed,',', german_shepard.facts)
