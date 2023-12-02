import os
os.system("clear")

print(20*"-")
print("WELCOME TO MOBILE LEGEND")
print(20*"-")
print("\n")

# CONSTRUCTOR ADALAH METHOD ATAU FUNGSI KHUSUS YANG DIBUAT DAN AKAN DIJALANKAN PERTAMA KALI PADA SAAT MEMBUAT CLASS 



# INISIALISAI OBJEK
class Hero:

    def __init__(self, name, health, damage, defense): # FUNGSI ATRIBUT OBJEK
        
        # INSTANCE VARIABEL 
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

        # PRIVATE VARIABEL INSTANCE 
        self.__private = "Ini adalah bentuk variabel privat"

        # PROTECTED VARIABEL INSTANCE
        self._protected = "Ini adalah bentuk variabel protected"

    # METHOD ATAU FUNGSI UNTUK MENYERANG

    def serang(self, enemy):
        print(f"{self.name} attacked {enemy.name}")
        print(f"Attack received by {self.damage}")
        
    # METHOD ATAU FUNGSI UNTUK BERTAHAN

    def bertahan(self, enemyDamage):
        attackReceive = (self.health + self.defense) - enemyDamage
        print("Health remains is " + str(attackReceive))
    

# AKSES OBJK 

Alucard = Hero("alucard",100,25,50)
Miya = Hero("Miya",100,40,20)


# MENAMPILKAN OBJEK

Alucard.serang(Miya)
Miya.bertahan(25)
print("\n")
Miya.serang(Alucard)
Alucard.bertahan(40)