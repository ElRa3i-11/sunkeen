class Item :
    def __init__(self,iname,weight) -> None:
        self.iname = iname
        self.weight = weight
class Weapon(Item) :
   def __init__(self, iname, weight,damage) -> None:
       super().__init__(iname, weight)
       self.damage = damage
   def __str__(self) -> str:
       return str(self.iname)
class Consumebale(Item) :
    def __init__(self, iname, weight,heal_value,base_dmg_add,):
        super().__init__(iname, weight)
        self.health_add = heal_value
        self.base_dmg_add = base_dmg_add
    def heal (self,h) : 
        h.health = h.health + self.health_add 
        h.health = min(100,h.health)
sword = Weapon("sword",50,10)
gold = Item("gold",10)
health_potion = Consumebale("Iris",5,50,0)