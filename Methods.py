import os
os.system("clear")



# METHOD ATAU FUNGSI TERBAGI MENJADI BEBERAPA BAGIAN YAITU :
# 1. METHOD ATAU FUNGSI DENGAN ARGUMEN ATAU PARAMETER
# 2. METHOD ATAU FUNGSI TANPA ARGUMEN ATAU PARAMETER
# 3. METHOD ATAU FUNGSI DENGAN RETURN

# INISIALISAI OBJEK
class Hero():

    jumlah = 0 # INI ADALAH CLASS VARIABEL

    def __init__(self, name, role, health, damage, level): # FUNGSI ATRIBUT OBJEK
        # INSTANCE VARIABEL 
        self.name = name
        self.role = role
        self.health = health
        self.damage = damage
        self.level = level
        Hero.jumlah +=1
    
    # METHOD TANPA ARGUMEN (VOID)

    def say (self):
        print(f"Hi my names's {self.name}")

    # METHOD DENGAN ARGUMEN

    def levelUp(self,up):
        self.level += up
    
    # METHOD DENGAN NILAI KEMBALIAN ATAU RETURN 

    def getLevel(self):
        return self.level



# AKSES OBJK 

hero1 = Hero("alucard","fighter",100,25,0)
hero2 = Hero("Miya","Marksman",100,40,1)


# MENAMPILKAN OBJEK

print(hero1.__dict__)
print(hero2.__dict__)
print(f"Jumlah total hero yang dimiliki ada = {Hero.jumlah}") # AKSES CLASS VARIABEL

# MENAMPILKAN METHOD ATAU FUNGSI TANPA ARGUMEN
hero1.say()

# INPUT ARGUMEN PADA METHOD ATAU FUNGSI LEVEL UP   
hero2.levelUp(1)

# MENAMPILKAN METHOD ATAU FUNGSI DENGAN NILAI KEMBALI ATAU RETURN
levelUp = hero2.getLevel()
print(f"Level saat ini adalah {levelUp}")


