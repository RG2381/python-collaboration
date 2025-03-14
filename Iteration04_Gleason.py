class Game:
    def __init__(self):
        self.running = True
        self.player = Player()
    
    def display_menu(self):
        print("\n--- Survival Game Menu ---")
        print("1. View Inventory")
        print("2. Check Energy")
        print("3. Gather Resources")
        print("4. Exit Game")
    
    def run(self):
        while self.running:
            self.display_menu()
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.player.show_inventory()
            elif choice == "2":
                self.player.check_energy()
            elif choice == "3":
                self.player.gather_resources()
            elif choice == "4":
                print("Exiting game...")
                self.running = False
            else:
                print("Invalid option, please try again.")

class Player:
    def __init__(self):
        self.inventory = []
        self.energy = 100
    
    def show_inventory(self):
        if self.inventory:
            print("\n--- Inventory ---")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
    
    def check_energy(self):
        print(f"Current Energy: {self.energy}/100")
    
    def gather_resources(self):
        if self.energy > 10:
            print("You gathered some wood and berries.")
            self.inventory.append("Wood")
            self.inventory.append("Berries")
            self.energy -= 10
        else:
            print("Not enough energy to gather resources. Rest to regain energy.")
    
if __name__ == "__main__":
    game = Game()
    game.run()

