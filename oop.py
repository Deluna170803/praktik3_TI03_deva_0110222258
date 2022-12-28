#oop itu sebuah paradigma
class Hero:
    name = "Allucard"
    hp = 3000
    damage = 200
    defense = 100

    def __init__ (self, name, hp, damage, defense):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense= defense

    def attack(self, target):
        target.hp = target.hp - self.damage
        print("sisa HP", target.name, "=", target.hp)

#Inisialisasi class hero
hero1 = Hero("Hayabusa", 2000, 300, 15)
hero2 = Hero("Atlas", 3000, 50, 300)

hero1.attack(hero2)
hero2.attack(hero1)
print(hero2.name)
