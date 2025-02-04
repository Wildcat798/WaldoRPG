class Unit:
    def __init__(self, name, position, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.position = position #[1,1]

    def get_hit(self, power):
        self.health = self.health - power        

    def attack(self, enemy):           
        enemy.get_hit(self.attack_power)
    
    def move(self, dir):
        if dir == "up":
            self.position = [self.position[0], self.position[1]-1]
        elif dir == "down":
            self.position = [self.position[0], self.position[1]+1]
        elif dir == "left":
            self.position = [self.position[0]-1, self.position[1]]
        elif dir == "right":
            self.position = [self.position[0]+1, self.position[1]]

class Player(Unit):
    def __init__(self, name, position, health = 100, attack_power = 20):
        super().__init__(name,position,health,attack_power)
        self.inventory = []
    
    def __str__(self):
        inv = ""
        for ivt in self.inventory:
            inv += " "+ivt.name
        return """
            Health:%s
            position: %s
            inventory: %s
        """ % (self.health, self.position,inv )
    
    def pickup_item(self, item):
        self.inventory.append(item)
        item.get_picked_up(self)