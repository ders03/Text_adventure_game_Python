from weapon import Weapon


class Blaster(Weapon):
    def __init__(self):
        super().__init__("Blaster")
        self.name = "Blaster"
        self.damage = 10
        self.cost = 2

    def ultimate_damage(self):
        return self.damage + 5

def main():
    Blaster

if __name__ == "__main__":
    main()
