from weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword")
        self.name = "Sword"
        self.damage = 5
        self.cost = 5

    def ultimate_damage(self):
        return self.damage*10

def main():
    Sword

if __name__ == "__main__":
    main()
