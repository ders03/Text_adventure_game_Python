from potion import Potion

class MagicElixir(Potion):
    def __init__(self):
        super().__init__("MagicElixir")
        self.name = "MagicElixir"
        self.benefit = 20

def main():
    MagicElixir
    
if __name__ == "__main__":
    main()
