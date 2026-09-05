import os
import pyfiglet
from Rooms import ROOMS , current_room_name
from item import sword , gold , health_potion
from entities import Player 
from shared import log , console 
import readchar
from ascii_map import MAP

os.system('clear')
console.print("\n\nLoading ..... ",style="bold blue",justify="center")


def reward_list():
    player_loot = p1.place["loot"]
    Y = ""  
    for i, x in player_loot.items():
        Y = Y + i + " " + str(x) + ", "
    return Y
## clear then rewrite all the text in the terminals
def redraw(view):
    os.system('clear')
    console.print(pyfiglet.figlet_format("The Sunkeen ", justify="center", width=150,))
    console.print("[bold italic magenta] Commands:[WASD] Movement [A] Attack [S] Stats [M] Map [H] Heal [C] Collect [/]",justify="center")
    console.print(f"\n\n[bold]Current room:[/] [bold blue] {current_room_name}[/]   [bold]Enemy:[/]  [bold blue]{p1.place['enemy']}[/]",justify="center")
    console.print(f"[bold]Room Rewards:[/] [bold blue] {reward_list()}[/]",justify="center")
    console.print("-" * 40)
    console.print("[bold reverse]Log :[/]")
    console.print("-" * 5)
    console.print(f"[bold]Your HP:[/] {health_bar(p1.health, p1.max_health)}",)
    if p1.place["enemy"] is not None:
        e = p1.place["enemy"]
        console.print(f"\n[bold]{e.name} HP:[/] {health_bar(e.health, e.max_health)}\n",)
    if view == "log" :
        for line in log:
            console.print(line)
        console.print("-" * 40)
    elif view == "map" :
            print(MAP)
    else :
        p1.display_stats()
def health_bar(current, max_hp, length=20):
    ratio = max(0, min(current / max_hp, 1))
    filled = int(length * ratio)
    empty = length - filled
    color = "green" if ratio > 0.5 else "yellow" if ratio > 0.2 else "red"
    bar = "█" * filled + "░" * empty
    return f"[{color}]{bar}[/] {current:.0f}/{max_hp}"

####

p1=Player("Rommel",100,5
          ,{
              "gold" : 100 ,
              "healing potion" : 2,              
          }
          ,1,
          ROOMS["starting room"],
          sword,50,100,100)

##
def loot():
    player_loot = p1.inventory_list
    loots = p1.place["loot"]
    for item1 , quantity1 in player_loot.items() :
        for item2 , quantity2 in loots.items() :
                if item2 == item1 :
                    X = quantity1 + quantity2
                    p1.inventory_list[item1] = X
                    p1.place["loot"][item1] = 0
    log.append("[bold green] -> Rewards collected [/]")
             
def heal():
    if p1.inventory_list["healing potion"] > 0 and p1.health < 100  :
        health_potion.heal(p1)
        p1.inventory_list["healing potion"] = p1.inventory_list["healing potion"] - 1
        log.append("[bold green]Heal succsefuly ![/]")
    else :
        log.append("[bold magenta]Ethier you dont Have healing potion , Or your health is 100[/]")
    redraw("log") 
def action_place(p,s) :
    if p1.place["exit"][p] is not None :
        p1.place = ROOMS[p1.place["exit"][p]]
        global current_room_name
        current_room_name = p1.place["name"]
        log.append(f"[bold] -> Moved into [bold cyan] {current_room_name} [/]")

    else :
        log.append("[bold italic red] -> Path is Blocked [/]")
    redraw(s)
##


class Game () :
    def run(self):
        redraw("log")
        while p1.health > 0 :
            key = readchar.readkey()
            if key == "a" :
                if  p1.place["enemy"] is not None :
                    p1.attack(p1.place["enemy"])
                else :
                    log.append("[bold] No enemies in room [/]")
                redraw("log")
            elif key in {"z","s","q","d"} :
                action_place(key,"log")
            elif key == "e" :
                redraw("stats")
            elif key == "m" :
                redraw("map")
            elif key == "h":
                heal()
            elif key == "c" :
                loot()
                redraw("log")
            else :
                log.append("[bold italic red underline]INVALID COMMAND[/]")
                redraw("log") 


game = Game()
game.run()
