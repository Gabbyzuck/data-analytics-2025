#Day5 Daily Challenge
class Farm:
    def __init__(self, name, animal, inventory):
        self.name = name
        self.animal = animal
        self.inventory = {}

    def add_animal(self, animal, count = 1):
        if animal in self.inventory:
            self.inventory[animal] += count
        else:
            self.inventory[animal] = count
        
    def get_info(self):  
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.inventory.items():  
           info += f"{animal} : {count}\n"  # List each animal  
        info += "\n    E-I-E-I-O!"  # End message  
        return info  

        # print(f"{self.name}'s farm")
        # print(f"{self.animal}: {self.inventory}")
        # print("E-I-E-I-O")

    # def get_info(self):
    #     print()



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
# print(macdonald.get_info())