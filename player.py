from weapon import Weapon
from sword import Sword
from blaster import Blaster
from potion import Potion
from magicelixir import MagicElixir

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.manna = 100

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_manna(self):
        return self.manna

    def suffer_damage(self, damage):
        self.health-=int(damage)
        if self.health<0:
            self.health = 0

    def attack(self, opp, weapon, is_ultimate=False):
        if self.manna >= weapon.get_cost() and is_ultimate != False:
            self.manna = 0
            opp.suffer_damage(weapon.ultimate_damage())
        if self.manna < 0:
            self.manna = 0
        if self.manna >= weapon.get_cost():
            self.manna -= weapon.get_cost()
            opp.suffer_damage(weapon.get_damage())

    def drink(self, potion):
        if Player.get_health(self)<100:
            self.health+=potion.drink()
        else:
            potion.drink()

def main():
    Player

if __name__ == "__main__":
    main()
