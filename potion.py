class Potion:
    def __init__(self, name, benefit=None):
        self.name = name
        if benefit is None:
            benefit = 10
        self.benefit = benefit

    def get_name(self):
        return self.name

    def get_benefit(self):
        return self.benefit

    def drink(self):
        x = self.benefit
        self.benefit=0
        return x

def main():
    Potion

if __name__ == "__main__":
    main()
