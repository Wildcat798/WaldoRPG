# Below in the items category you'll be setting and defining the item, potion, self.
# Mainly you'll be initializing (init) in order to use them to go along with other parts of the game. 

class Item:
    def __init__(self, name, position):
        self.position = position
        self.name = name
    
class Potion(Item):
    def __init__(self, name, position):
        super().__init__(name,position)
        self.owner = None
    
    def use(self):
        self.owner.health += 100
        for i in range(len(self.owner.inventory)):
            if self.owner.inventory[i] == self:
                del self.owner.inventory[i]
        self.owner = None

    
    def get_picked_up(self,owner):
        self.owner = owner
        self.position = [-555555,-555555]