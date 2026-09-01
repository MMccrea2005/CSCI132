class pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def describe(self):
        print(f'{self.name} is a {self.age}-year-old {self.species}.')

pet1 = pet('Gerald', 'Dog', 5)
pet2 = pet('Frank', 'Giraffe', 27)
pet3 = pet('Jeff', 'Lizard', 5)

def main():
    pet1.describe()
    pet2.describe()
    pet3.describe()

main()
