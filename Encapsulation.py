import os
os.system("clear")

"""
ENKAPSULASI ADALAH KONSEP YANG DBUAT UNTUK MENDEFINISIKAN SUATU ATRIBUT ATAU FUNGSI PADA SEBUAH CLASS UNTUK MENENTUKAN HAK AKSES
UNTUK DIAKSES SECARA GLOBAL DAN PRIVATE
"""

# CONTOH :

class Hero():

    # PRIVATE CLASS VARIABEL
    __numberOfHeroes = 0
    
    def __init__(self, name, health, damage, role, level):

        # ATRIBUT DIBAWAH INI BERSIFAT PRIVATE, HANYA BISA DI AKSES MENGGUNAKAN GETTER & SETTER METHOD
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__role = role
        self.__level = level
        Hero.__numberOfHeroes +=1
        

    # DIBAWAH INI ADA 2 KONSEP ENKAPSULASI ATAU CARA MEMBUAT GETTER & SETTER :

    # 1. KONSEP STANDART PARADIGMA OOP

    def getName(self):
        print(f"Hero name : {self.__name}")

    
    
    def attkrecieve(self,attackReceive):
        self.__health -=attackReceive
        healthRemains = self.__health
        print(f"Health remains : {healthRemains}")

    def healthReamins(objek, enemy, damage): # SELF BISA DIGANTI DENGAN KATA APA SAJA CONTOH DISAMPING DIGANTI DENGAN KATA OBJEK
        print(f"{objek.__name} received attack from {enemy} with damage {damage}")

    # 2. KONSEP BAWAAN DARI PYTHON

    @property # DECOORATOR YANG BERFUNGSI UNTUK MENGUBAH METHOD ATAU FUNGSI MENJADI ATRIBUT OBJEK
    def role(self):
        return self.__role
    
    @property
    def level(self):
        pass

    @level.setter
    def level(self,input):
        self.__level = input
        

    # DIBAWAH INI ADALAH STATIC METHOD UNTUK MENGAKSES PRIVATE CLASS VARIABEL DAN OBJEK
    @staticmethod
    def getNumber():
        return Hero.__numberOfHeroes
    

    # DIBAWAH INI ADALAH CLASS METHOD UNTUK MENGAKSES PRIVATE CALSS VARIABEL DAN OBJEK
    # REKOMENDASI PAKAI INI SAJA, KARENA LEBIH SIMPEL TANPA MENGUBAH NAMA CLASS
    @classmethod
    def getNumber2(cls):
        return cls.__numberOfHeroes


print("Dibawah ini contoh implementasi objek dengan konsep enkapsulasi standart OOP :\n")

harley = Hero("Harley", 100, 20, "Mage", 1)
print(f"Heroes number : {Hero.getNumber()}") # AKSES DENGAN OBJEK
harley.getName() # AKSES GETTER MENGGUNAKAN PARADIGMA STANDART OOP
harley.healthReamins("Martis", 40) # AKSES GETTER MENGGUNAKAN PARADIGMA STANDART OOP
harley.attkrecieve(40) # AKSES SETTER MENGGUNAKAN PARADIGMA STANDART OOP


print("\n=====================================================\n")

martis = Hero("Martis", 100, 40, "Fighter", 1)
print(f"Heroes number : {Hero.getNumber2()}") # AKSES DENGAN CLASS
martis.getName() # AKSES GETTER MENGGUNAKAN PARADIGMA STANDART OOP
martis.healthReamins("Harley",20) # AKSES GETTER MENGGUNAKAN PARADIGMA STANDART OOP
martis.attkrecieve(20) # AKSES SETTER MENGGUNAKAN PARADIGMA STANDART OOP

print("\nDibawah ini contoh implementasi objek dengan konsep enkapsulasi pyton :\n")

print(f"Heroes role : ",harley.role)
harley.level = 2
print(f"Heroes level = ", harley.level)