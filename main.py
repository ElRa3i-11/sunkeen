import os
import pyfiglet
from Rooms import ROOMS , current_room_name
from item import sword , gold
from entities import Player 
from shared import log , console 


os.system('clear')
console.print("\n\nLoading ..... ",style="bold blue",justify="center")
import pywhatkit as pwk
### image to ascii
if __name__ == "__main__":
    input_image = "asciimap.png"
    output_image = "ascii_map"

    pwk.image_to_ascii_art(input_image, output_image)


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
##


class Game () :
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
