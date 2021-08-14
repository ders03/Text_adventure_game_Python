

class Weapon:
    def __init__(self, name, damage=None, cost=None):
        self.name = name
        self.damage = damage
        self.cost = cost
        if self.damage == None:
            self.damage = 0
        if self.cost == None:
            self.cost = 0
        else:
            self.cost = cost

    def get_damage(self):
        return self.damage

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def ultimate_damage(self):
        return ultimate_damage()

def main():
    Weapon

if __name__ == "__main__":
    main()
