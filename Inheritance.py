import os
os.system("clear")


"""
INHERITANCE ADALAH BAGIAN DARI KONSEP OOP DIMANA SEBUAH CLASS BISA MEMILIKI SUPER ATAU INDUK CLASS DENGAN ATRIBUT, FUNGSI, DAN PERIAKU YANG SAMA
"""

class Hero():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def info(self):
        print("{} \t\n Health : {} \n Damage : {}".format(self.name,self.health,self.damage))

class Mage(Hero): # INI ADALAH KELAS MAGE YAITU KELAS TURUNAN DARI CLASS HERO
    def __init__(self, name):
        super().__init__(name, 100, 25)

        # SYNTAX UNTUK AKSES FUNGSI INFO PADA SUPERCLASS 
        super().info()
    
    # PAKAI SYNTAX DIBAWAH INI JUGA BISA UNTUK AKSES FUNGSI INFO PADA SUPERCLASS 

    #def info(self):
    #    return super().info()
        
class Support(Hero): # INI ADALAH KELAS MAGE YAITU KELAS TURUNAN DARI CLASS HERO
    def __init__(self, name):
        super().__init__(name, 100, 15)

    # DIBAWAH INI ADALAH CONTOH TEKNIK OVERRIDE ATAU TEKNIK MENIMPA SEBUAH FUNGSI ATAU METHOD    
    def info(self):
        print("{} \t\n Health : {} \n Damage : {} \t\n Role : Support".format(self.name,self.health,self.damage))


    # PAKAI SYNTAX DIBAWAH INI JUGA BISA UNTUK AKSES FUNGSI INFO PADA SUPERCLASS

    #def info(self):
    #    return super().info()


gord = Mage("Gord")
angela = Support("Angela")

#  DIBAWAH INI ADALAH UNTUK AKSES METHOD INFO PADA CLASS SUPPORT
angela.info()

