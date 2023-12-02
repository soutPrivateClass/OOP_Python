import os
os.system("clear")

"""
MULTIPLE INHERITANCE ADALAH SEBUAH KONSEP OOP DIMANA SEBUAH SUB CLASS BISA MEMILIKI LEBIH DARI SATU SUPER CLASS
"""

class Role:

    def setRole(self,input):
        self.role = input

    def showRole(self):
        print(f"{self.name} adalah hero dengan role {self.role}")
        

class Weapon:

    def setWeapon(self,input):
        self.weapon =input

    def showWeapon(self):
        print(f"{self.name} adalah hero dengan {self.weapon} sebagai senjatanya")

# DIBAWAH INI ADALAH CONTOH MULTIPLE INHERITANCE 
class Hero(Role,Weapon):
    
    def __init__(self, name):
        self.name = name
        

moskov = Hero("Moskov")
esme = Hero("Esme")


moskov.setRole("marksman")
moskov.setWeapon("tombak")
moskov.showRole()
moskov.showWeapon()

print(50*"-")

esme.setRole("roam")
esme.setWeapon("selendang")
esme.showRole()
esme.showWeapon()

