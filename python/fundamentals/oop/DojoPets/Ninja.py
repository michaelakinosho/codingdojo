"""
Author: Michael Akinosho
Date: October 29, 2021
"""
from Pet import Pet
from Dog import Dog

import random

class Ninja:
    def __init__(self, first_name, last_name,pet_treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_treats = pet_treats
        self.pet_food = pet_food
        self.pet = pet
        
    def display_Ninja_name(self):
        print("Pet owner: {} {}, pet's name: {} is a {}".format(self.first_name,self.last_name,self.pet.pet_name,self.pet.type))
        return self
    
    def walk(self):
        self.pet.play()
        num = random.randint(0,len(self.pet.tricks)-1)
        print("{} my {} just finished his {} activity.".format(self.pet.pet_name,self.pet.type,self.pet.tricks[num]))
        return self
    
    def feed(self):
        self.pet.eat()
        num = random.randint(0,len(self.pet_food)-1)
        print("{} my {} just finished his {} meal.".format(self.pet.pet_name,self.pet.type,self.pet_food[num]))
        return self
    
    def bathe(self):
        self.pet.noise()
        num = random.randint(0,len(self.pet.sound)-1)
        print("{} my {} while bathing makes his {} sound.".format(self.pet.pet_name,self.pet.type,self.pet.sound[num]))
        self.pet.sleep()
        return self

if __name__ == "__main__":
    pet = {'name':'Bruno Mars','type':'dog','tricks':['jumping','rolling','playing dead'],'health':100,'energy':50,'sound':['sad','happy','not fun','pet paradise']}
    
    mypet = Pet(pet)
    myNinjaPet = Ninja('Oscar','Robinson',['Toy','Rope','Ball'],['Blue Diamond',"Farmers' Pet"],mypet)
    myNinjaPet.display_Ninja_name().feed().walk().bathe()
    print('\n')
        
    pet1 = {'name':'Snoop Doggy','type':'PitBull','tricks':['jumping','rolling','playing dead'],'health':100,'energy':50,'sound':['sad','happy','not fun','pet paradise']}

    mypet2 = Dog(pet1)
    myNinjaPetDog = Ninja('Oscar','Robinson',['Toy','Rope','Ball'],['Blue Diamond',"Farmers' Pet"],mypet2)
    myNinjaPetDog.display_Ninja_name().feed().walk().bathe()