#########################
#                       #
#  MAIN GAME CODE FILE  #
#                       #
#########################

# Required libraries import
from rich import print
import random, os, json
from modules import renderer, fighting

# Variables
player_hp = 100
hp_potions = 2

# GAME SAVE
saveFileNum = 1
def save():
    game_state = {
        "player": {"y": renderer.player_y, "x": renderer.player_x, "hp": player_hp},
        "hp potions": hp_potions,
        "map": renderer.MAP
    }

    filename = "RPG/save.json"
    if os.path.exists(filename):
        print("Are you sure? This will erase your last save!")
        choice = input("Y/N > ")
        if choice == "Y":
            with open(filename, "w") as f:
                json.dump(game_state, f)
            print("Game state saved.")
            input()
        else:
            print("Game saving cancelled.")
            input()
    else:
        with open(filename, "w") as f:
            json.dump(game_state, f)
        print("Game state saved.")
        input()

# GAME LOAD
def load():
    filename = "RPG/save.json"
    if os.path.exists(filename):
        print("Are you sure? This will erase your unsaved progress!")
        choice = input("Y/N > ")
        if choice == "Y":
            with open(filename, "r") as f:
                game_state = json.load(f)
                global player_hp, hp_potions
                renderer.player_y = game_state["player"]["y"]
                renderer.player_x = game_state["player"]["x"]
                player_hp = game_state["player"]["hp"]
                hp_potions = game_state["hp potions"]
                renderer.MAP = game_state["map"]

            print("Game state loaded.")
            input()
        else:
            print("Game loading cancelled.")
            input()
    else:
        print("No game save found. A new game will be started.")
        input()


####################
# GAME MENU + LOOP #
####################
def start():
    renderer.genMap()
    while not fighting.dead:
        renderer.renderMap()
        print()
        print()
        print("w - up")
        print("a - left")
        print("s - down")
        print("d - right")
        print("1 - save game")
        print("2 - quit game ([bold red]DOESN'T SAVE GAME STATE![/bold red])")
        choice = input("> ")
        if choice == "W" or choice == "w":
            if renderer.player_y > 0:
                renderer.player_y -= 1
        elif choice == "A" or choice == "a":
            if renderer.player_x > 0:
                renderer.player_x -= 1
        elif choice == "S" or choice == "s":
            if renderer.player_y < renderer.MAP_HEIGHT:
                renderer.player_y += 1
        elif choice == "D" or choice == "d":
            if renderer.player_x < renderer.MAP_WIDTH:
                renderer.player_x += 1
        elif choice == "1":
            save()
        elif choice == "2":
            print("Are you sure? All progress since last save will be lost.")
            choice = input("Y/N > ")
            if choice == "Y":
                exit()
            else:
                print("Game quit cancelled.")
        else:
            print("This option doesn't exist.")

if __name__ == "__main__":

    while True:                                 # MAIN MENU LOOP
        renderer.clear()
        print("[bold]TERMINALRPG[/bold]")
        print()
        print()
        print("1 - New Game")
        print("2 - Load Game")
        print("3 - Quit game")
        try:
            choice = int(input("> "))
        except ValueError:
            choice = 0 


        if choice == 1:
            game_state = {
            "player": {"y": renderer.player_y, "x": renderer.player_x, "hp": player_hp},
            "hp potions": hp_potions
            }
            break
        elif choice == 2:
            load()
            break
        elif choice == 3:
            exit()
        else:
            renderer.clear()
            print("This option doesn't exist.")
    
    start()