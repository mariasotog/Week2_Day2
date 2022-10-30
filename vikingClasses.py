from random import choice

# Soldier

class Soldier:
    
    def __init__(self, health, strength): 
        self.health = health
        self.strength = strength
    
    def attack(self):  
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking

class Viking(Soldier):
    
    def __init__(self, name, health, strength): 
        self.name = name
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "{} has died in act of combat".format(self.name)
        else:
            return "{} has received {} points of damage".format(self.name, damage)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received {} points of damage".format(damage)

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        return None

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        return None
    
    def vikingAttack(self):
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        ataque = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        else:
            pass
        return ataque

    def saxonAttack(self):
        viking = choice(self.vikingArmy)
        saxon = choice(self.saxonArmy)
        ataque = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        else:
            pass
        return ataque