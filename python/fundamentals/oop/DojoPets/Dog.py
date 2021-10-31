"""
Author: Michael Akinosho
Date: October 29, 2021
"""
from Pet import Pet

class Dog(Pet):
    def __init__(self, dog):
        self.pet_name = dog['name']
        self.type = dog['type']
        self.tricks = dog['tricks']
        self.health = dog['health']
        self.energy = dog['energy']
        self.sound = dog['sound']
        
if __name__ == "__main__":
    pet = {'name':'Bruno Mars','type':'French Bulldog','tricks':['jumping','rolling','playing dead'],'health':100,'energy':50,'sound':['sad','happy','not fun','pet paradise']}
    myPet = Dog(pet)
    myPet.display_Pet_Name()