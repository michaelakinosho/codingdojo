"""
Author: Michael Akinosho
Date: October 29, 2021
"""
class Pet:
    def __init__(self, pet):
        self.pet_name = pet['name']
        self.type = pet['type']
        self.tricks = pet['tricks']
        self.health = pet['health']
        self.energy = pet['energy']
        self.sound = pet['sound']
        
    def display_Pet_Name(self):
        print("{}".format(self.pet_name))
        return self
    
    def sleep(self):
        self.energy += 25
        print('{} is ready to sleep.'.format(self.pet_name))
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        self.energy -= 10
        return self
        
    def noise(self):
        return self
    
if __name__ == "__main__":
    pet = {'name':'Bruno Mars','type':'dog','tricks':['jumping','rolling','playing dead'],'health':100,'energy':50,'sound':['sad','happy','not fun','pet paradise']}
    myPet = Pet(pet)
    myPet.display_Pet_Name()