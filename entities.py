
from rich.table import Table
from item import * 
from shared import log , console 
from random import choice

class Sprite :
    def __init__(self,name,health,base_dmg,level,max_health):
        self.health = health
        self.base_dmg = base_dmg
        self.level = level
        self.name = name
        self.max_health = max_health

    def display_stats(self) :
        table=Table(title="Stats",style="bold red")

        table.add_column("Stat",style="bold magenta")
        table.add_column("Value",style="bold cyan")

        table.add_row("Name",f"{self.name}")
        table.add_row("Level",f"{self.level}")
        table.add_row("Xp",f"{self.xp}")
        table.add_row("Weapon",f"{self.weapon}")
        table.add_row("gold",f"{self.inventory_list["gold"]}")
        table.add_row("healing potion",f"{self.inventory_list["healing potion"]}")

        console.print(table)
class Player(Sprite) :

    def __init__(self,name,health, base_dmg, inventory_list, level,place,weapon,xp,lvl_req,max_health) -> None:
        super().__init__(name,health, base_dmg, level,max_health)
        self.inventory_list = inventory_list
        self.place = place
        self.weapon = weapon
        self.xp = xp
        self.lvl_req = lvl_req
    def level_up(self) :

        while self.xp >= self.lvl_req :
            self.level = self.level + 1
            self.xp = self.xp - self.lvl_req
            self.lvl_req = self.lvl_req + 10

    def player_attack(self,target) :
        log.append("[bold green underline] -> Hit Target ![/]")
        target.health = target.health - ((self.base_dmg+(self.level*0.1)) + self.weapon.damage)
        target.health = max(target.health,0)
        
    def counter_attack(self,target,) :
        d = choice([0,1,2,3])
        if d > 0 :
            log.append("[bold red underline] -> You got Hit ![/]")
        else :
            log.append("[bold blue] -> You Dogede Attack[/]")
        self.health = self.health - ((target.base_dmg+(self.level*0.1))*d)
        self.health = max(self.health,0)
        if self.health == 0 :
            console.print("[bold red underline] -> YOU DIED[/]")
            quit()

    def target_die (self,target) :
        self.xp = self.xp + target._xp
        self.level_up()
        log.append(f"[bold cyan] -> {self.place["enemy"]} is dead[/]")
        self.place["enemy"] = None

    def attack(self,target) :
        self.player_attack(target)
        if target.health > 0 :
            self.counter_attack(target)
        elif target.health <= 0 :
            self.target_die(target)
           
class Enemy(Sprite) :
    def __init__(self, name, health, base_dmg, level, reward,_xp,max_health) -> None:
        super().__init__(name, health, base_dmg, level,max_health)
        self.reward = reward
        self._xp = _xp
    def __str__(self) -> str:
        return str(self.name)




