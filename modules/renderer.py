#####################
#                   #
#  RENDERER MODULE  #
#                   #
#####################


#  Required libraries import
from rich import print
import random, os
from modules import fighting

# Variables etc.

MAP_HEIGHT = 20
MAP_WIDTH = 20

player_x = MAP_WIDTH // 2
player_y = MAP_HEIGHT // 2
PLAYER = "[blue]@[/blue]"
MAP = []
mapTemp = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Map generation code

def genMap():
    global MAP, mapTemp
    for y in range(0, MAP_HEIGHT):
        for x in range(0, MAP_WIDTH):
            if y == 0 or y == MAP_HEIGHT - 1:
                mapTemp.append("[bold]#[/bold]")
            elif x == 0 or x == MAP_WIDTH - 1:
                mapTemp.append("[bold]#[/bold]")
            else:
                number = random.randint(0, 15)
                if number < 5:
                    mapTemp.append("[green]A[/green]")
                elif number == 5:
                    mapTemp.append("[purple]*[/purple]")
                elif number == 6:
                    if x != player_x and y != player_y:
                        mapTemp.append("[red]$[/red]")
                    else:
                        mapTemp.append("[green].[/green]")
                else:
                    mapTemp.append("[green].[/green]")
        MAP.append(mapTemp)
        mapTemp = []

# Map rendering code

def renderMap():
    clear()
    global MAP
    for y in range(0, MAP_HEIGHT):
        for x in range(0, MAP_WIDTH):
            if x == player_x and y == player_y:
                print(PLAYER, end='')
                if MAP[y][x] == "[red]$[/red]":
                    fighting.encounter(y, x)
                    return
            else:
                print(MAP[y][x], end='')
        print("")
    print("[bold]#[/bold] - world border")
    print("[green]A[/green] - decorative trees")
    print("[purple]*[/purple] - decorative flowers")
    print("[red]$[/red] - enemy")
    print("[green].[/green] - grass")
    print("")
    print("")