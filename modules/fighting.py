#####################
#                   #
#  FIGHTING MODULE  #
#                   #
#####################


# Required libraries import
from rich import print
import random, os, main
from modules import renderer

inFight = False
dead = False

def encounter(y, x):
    renderer.clear()
    number = random.randint(0, 3)
    if number < 2:
        fightLoop("skeleton", random.randint(10, 15), 0, 0)
    elif number == 2:
        fightLoop("wolf", random.randint(20, 25), 1, 2.5)
    else:
        fightLoop("ghoul", random.randint(40, 50), 5, 25)

def death():
    global dead
    dead = True
    input("Press enter to clear save. ")
    if os.path.exists("save.json"):
        os.remove("save.json")


def fightLoop(encounterType:str, hp:int, healAmount:int, healChance:float):
    print(f"You are fighting a [red]{encounterType}[/red] which has [magenta]{hp}[/magenta] HP!")
    print(f"You have [lime]{main.player_hp}[/lime] HP.")
    input("Press enter to begin fighting. ")

    renderer.clear()
    while hp > 0 and main.player_hp > 0:
        print(f"[red]{encounterType}[/red]           [magenta]{hp} HP[/magenta]")
        for _ in range(0, 5):
            print()
        print(f"[light blue]You[/light blue]           [lime]{main.player_hp} HP[/lime]")
        print()
        print("1 - attack - 5 to 10 damage")
        print(f"2 - heal - 10 to 20 HP - [lime]{main.hp_potions}[/lime] potions left")
        choice = int(input("> "))

        if choice == 1:
            damage = random.randint(5, 10)
            main.player_hp -= healAmount * 2 + 5 # Player damage formula
            hp -= damage
            renderer.clear()
            print(f"You received [red]{healAmount * 2 + 5}[/red] damage!")
            print(f"[red]{encounterType}[/red] received [magenta]{damage}[/magenta] damage!")
        elif choice == 2:
            if main.hp_potions > 0:
                heal = random.randint(10, 20)
                main.player_hp += heal
                main.hp_potions -= 1
                print(f"You regenerated [lime]{heal}[/lime] HP!")
                if 0 < random.randint(0, 100) <= healChance:
                    hp += healAmount
                print(f"[red]{encounterType}[/red] regenerated [magenta]{healAmount}[/magenta] HP!")
            else:
                print("You don't have any potions!")
        else:
            print("Invalid choice!")
        
        input()

    if main.player_hp == 0:
        print("[bold red]YOU DIED[/bold red]")
        death()
    else:
        print(f"[lime] You killed the {encounterType}![/lime]")
        reward = random.randint(1, 3)
        print(f"You got [bold yellow]{reward}[/bold yellow] potions.")
        main.hp_potions += reward
        renderer.MAP[renderer.player_y][renderer.player_x] = "[lime].[/lime]"
        input()
        renderer.clear()
        renderer.renderMap()
