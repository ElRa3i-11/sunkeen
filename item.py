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
sword = Weapon("sword",50,10)
gold = Item("gold",10)