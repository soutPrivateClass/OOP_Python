import os
os.system("clear")



# CONSTRUCTOR ADALAH METHOD ATAU FUNGSI KHUSUS YANG DIBUAT DAN AKAN DIJALANKAN PERTAMA KALI PADA SAAT MEMBUAT CLASS 



# INISIALISAI OBJEK
class Hero:

    jumlah = 0 # INI ADALAH CLASS VARIABEL

    def __init__(self, name, role, health, damage, level): # FUNGSI ATRIBUT OBJEK
        # INSTANCE VARIABEL 
        self.name = name
        self.role = role
        self.health = health
        self.damage = damage
        self.level = level
        Hero.jumlah +=1



# AKSES OBJK 

hero1 = Hero("alucard","fighter",100,25,0)
hero2 = Hero("Miya","Marksman",100,40,1)


# MENAMPILKAN OBJEK

print(hero1.__dict__)
print(hero2.__dict__)
print(f"Jumlah total hero yang dimiliki ada = {Hero.jumlah}") # AKSES CLASS VARIABEL