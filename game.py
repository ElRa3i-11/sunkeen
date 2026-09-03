
from collections import deque
import os
from random import choice
import pyfiglet
from rich.console import Console
from rich.table import Table


log = deque(maxlen=3)
console = Console()
os.system('clear')
console.print("\n\nLoading ..... ",style="bold blue",justify="center")
import pywhatkit as pwk
### image to ascii
if __name__ == "__main__":
    input_image = "asciimap.png"
    output_image = "ascii_map"

    pwk.image_to_ascii_art(input_image, output_image)

### Items
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
### Sprites

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

        table.add_row("Name",f"{p1.name}")
        table.add_row("Health",f"{p1.health:.0f}")
        table.add_row("Level",f"{p1.level}")
        table.add_row("Xp",f"{p1.xp}")
        table.add_row("Weapon",f"{p1.weapon}")

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

        while p1.xp >= self.lvl_req :
            p1.level = p1.level + 1
            p1.xp = p1.xp - self.lvl_req
            self.lvl_req = self.lvl_req + 10

    def attack(self,target) :
        if target.health > 0 :
            log.append("[bold magenta underline]Hit Target ![/]")
            target.health = target.health - ((self.base_dmg+(self.level*0.1)) + p1.weapon.damage)
            target.health = max(target.health,0)
            ### there is a chance that the target will attack
            d = choice([0,1,2,3])
            if d > 0 :
                log.append("[bold red underline]You got Hit ![/]")
            else :
                log.append("[bold blue]You Dogede Attack[/]")
            self.health = self.health - ((target.base_dmg+(self.level*0.1))*d)
            self.health = max(self.health,0)
            log.append(f"[bold]Enemy Health : [/]{target.health:.1f}")
            if target.health == 0 :
                self.xp = self.xp + target._xp
                p1.level_up()
                log.append(f"[bold cyan]{p1.place["enemy"]} is dead[/]")
                del target
                p1.place["enemy"] = None
            elif self.health == 0 :
                console.print("[bold red underline]YOU DIED[/]")
                quit()
class Enemy(Sprite) :
    def __init__(self, name, health, base_dmg, level, reward,_xp,max_health) -> None:
        super().__init__(name, health, base_dmg, level,max_health)
        self.reward = reward
        self._xp = _xp
    def __str__(self) -> str:
        return str(self.name)

slime1 = Enemy("Slime",40,5,2,"nothing",100,40)
slime2 = Enemy("Slime",40,5,2,"nothing",100,40)
manticore = Enemy("Manticore",100,20,15,"nothing",500,100)
minotaur = Enemy("Minotaur",200,10,5,"nothing",200,200)
## The rooms data
ROOMS = {
    "starting room":{
        "name" : "starting room",
        "enemy" : None,
        "gold" : 10,
        "exit" : {
            "left" : "Hallway",
            "up" : None,
            "down":None,
            "right":None
        }

    },
    "Hallway":{
        "name" : "Hallway (section 1)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :"Hallway2",
            "up" : "Treasury room" ,
            "down":"Ferdinand room",
            "right":"starting room"
        }

    },
    "Hallway2":{
        "name" : "Hallway (section2)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :"Hallway3",
            "up" : "Hallway4" ,
            "down":None,
            "right":"Hallway",
        }

    },
    "Hallway3":{
        "name" : "Hallway (section3)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :None,
            "up" : None,
            "down":"Minotaur room",
            "right":"Hallway2",
        }

    },
    "Hallway4":{
        "name" : "Hallway (upper_section)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :"Manticore room",
            "up" : None ,
            "down":"Hallway2",
            "right":None,
        }

    },

    "Ferdinand room":{
        "name" : "Ferdinand room",
        "enemy" : slime1,
        "gold" : 50,
        "exit" : {
            "left" :None,
            "up" : "Hallway" ,
            "down":None,
            "right":None
        }
    },
    "Treasury room":{
        "name" : "Treasury room",
        "enemy" : slime2,
        "gold" : 50,
        "exit" : {
            "left" :None,
            "up" : None ,
            "down":"Hallway",
            "right":None
        }

    },
    "Minotaur room":{
        "name" : "Minotaur Room",
        "enemy" : minotaur,
        "gold" : 300,
        "exit" : {
            "left" :None,
            "up" : None ,
            "down":"Hallway3",
            "right":None
        }

    },
    "Manticore room":{
        "name" : "Manticore Room",
        "enemy" : manticore,
        "gold" : 200,
        "exit" : {
            "left" :"Hallway4",
            "up" : None ,
            "down":None,
            "right":None
        }

    }
}
current_room_name = ROOMS["starting room"]["name"]
p1=Player("Rommel",100,5,[(gold,100)],1,ROOMS["starting room"],sword,50,100,100)
##
def health_bar(current, max_hp, length=20):
    ratio = max(0, min(current / max_hp, 1))
    filled = int(length * ratio)
    empty = length - filled
    color = "green" if ratio > 0.5 else "yellow" if ratio > 0.2 else "red"
    bar = "█" * filled + "░" * empty
    return f"[{color}]{bar}[/] {current:.0f}/{max_hp}"

def action_place(p,s) :
    if p1.place["exit"][p] is not None :
        p1.place = ROOMS[p1.place["exit"][p]]
        global current_room_name
        current_room_name = p1.place["name"]
        log.append(f"you are now in [bold cyan]!! {current_room_name} !![/]")

    else :
        log.append("Path is Blocked")
    redraw(s)
#
## clear then rewrite all the text in the terminal
def redraw(view):
    os.system('clear')
    console.print(pyfiglet.figlet_format("The Sunkeen ", justify="center"), style="bold")
    console.print("[bold italic magenta] Commands: attack, movement:{up, down, right, left}, stats, map[/]")
    console.print(f"\n\n[bold]Current room:[/] [bold red] {current_room_name}[/]   [bold]Enemy:[/]  [bold red]{p1.place['enemy']}[/]")
    console.print("-" * 40)
    console.print("[bold reverse]Log :[/]")
    console.print("-" * 5)
    console.print(f"[bold]Your HP:[/] {health_bar(p1.health, p1.max_health)}")
    if p1.place["enemy"] is not None:
        e = p1.place["enemy"]
        console.print(f"\n[bold]{e.name} HP:[/] {health_bar(e.health, e.max_health)}\n")
    if view == "log" :
        for line in log:
            console.print(line)
        console.print("-" * 40)
    elif view == "map" :
        with open(output_image + ".txt", "r") as f:
            print(f.read())
    else :
        p1.display_stats()

##
class Game () :
    ## the game loop
    def run(self):
        redraw("log")
        while p1.health > 0 :
            action = input(":")
            if action == "attack" :
                if  p1.place["enemy"] is not None :
                    p1.attack(p1.place["enemy"])
                else :
                    log.append("this room is empty ")
                redraw("log")
            elif action in {"up","down","left","right"} :
                action_place(action,"log")
            elif action == "stats" :
                redraw("stats")
            elif action == "map" :
                redraw("map")
            else :
                log.append("INVALID COMMAND")
                log.append("INVALID COMMAND")
                log.append("INVALID COMMAND")

game = Game()
game.run()
