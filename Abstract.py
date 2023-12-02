import os
os.system("clear")


"""
UNTUK PENGIMPLEMENTASIAN SEBUAH ABSTRACT CLASS MEMAKSA CHILD CLASS HARUS MEMILIKI
METHOD SERTA PERILAKU YANG SAMA DENGAN SUPER CLASS
"""



# abc adalah abstract base class 
from abc import ABC,abstractmethod


class Hero(ABC):

    @abstractmethod
    def health(self,health):
        self.health = health
        print(f"Hero ini memiliki helath {self.health}")

class Role(Hero):

    def health(self,health):
        self.health = health
        print(f"Hero ini memiliki helath {self.health}")

class Weapon(Hero):

    def health(self,health):
        self.health = health
        print(f"Hero ini memiliki helath {self.health}")

martis = Role()
martis.health(100)

