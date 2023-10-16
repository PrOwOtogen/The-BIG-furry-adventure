from rich.console import Console

from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

import time
import sys
import os
import random
import json
import math


from utils.PlayerEnyClass import myp as myp
from utils.PlayerEnyClass import Enemy as Enemy
from utils.Stats import *
from utils.Textgen import *
from utils.functions import *


##item dictionary


"""
MAP LAYOUT

LOCATIONCODE : {
    "name" : "location name",
    "description" : "description of location",
    "exits" : {"north": "OTHER LOCATIONCODE"}
    "enemies" : [],
    "items" : [],
    "NPC" : [],
}
"""

mapd = {}


def printn(c, t=0.8):
    ##typewriter effect
    for char in c:
        sys.stdout.write(char)
        sys.stdout.flush()
        if t == 0:
            t = random.randint(0, 5)
        time.sleep(t / 100)


def impjson():
    ##import json
    with open("texts/Text.json", "r") as f:
        data = json.load(f)
        return data


##main menu with rich:
def main_menu():
    ##make startup
    startup()
    global JSON
    JSON = impjson()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Main Menu", justify="center", style="cyan", no_wrap=True)
    table.add_row("1. Start Game")
    table.add_row("2. load Game")
    table.add_row("3. Help")
    table.add_row("4. Exit Game")
    table.add_row("5. Credits")
    print(table)
    choice = Prompt.ask("What do you want to do?", choices=["1", "2", "3", "4", "5"])
    if choice == "1":
        start_game()
    elif choice == "2":
        load_game()
    elif choice == "3":
        helps()
    elif choice == "4":
        os.system("exit")
    elif choice == "5":
        credits()

        ##start game


def load_game():
    global mapd
    which = input("please enter the path to your JSON save file: ")
    if os.path.exists(which):
        with open(which, "r") as f:
            try:
                data = json.load(f)
                # put everything in myp.player
                myp.name = data["player"]["name"]
                myp.health = data["player"]["health"]
                myp.weight = data["player"]["weight"]
                myp.defense = data["player"]["defense"]
                myp.height = data["player"]["height"]
                myp.clean = data["player"]["clean"]
                myp.filth = data["player"]["filth"]
                myp.speed = data["player"]["speed"]
                myp.attack = data["player"]["attack"]
                myp.lust = data["player"]["lust"]
                myp.species = data["player"]["species"]
                myp.armor = data["player"]["armor"]
                myp.inventory = data["player"]["inventory"]
                myp.location = data["player"]["location"]
                myp.status_effects = data["player"]["status_effects"]
                myp.health_issues = data["player"]["health_issues"]
                myp.addedsizes = data["player"]["sizes"]
                myp.normalsizes = data["player"]["normalsizes"]
                myp.quests = data["player"]["quests"]
                myp.gold = data["player"]["gold"]
                myp.xp = data["player"]["xp"]
                myp.level = data["player"]["level"]
                myp.max_health = data["player"]["max_health"]
                myp.max_weight = data["player"]["max_weight"]
                myp.max_lust = data["player"]["max_lust"]
                myp.max_xp = data["player"]["max_xp"]
                myp.furcolor = data["player"]["furcolor"]
                myp.furtexture = data["player"]["furtexture"]
                myp.lastshower = data["player"]["lastshower"]
                myp.lastfood = data["player"]["lastfood"]
                myp.lastsleep = data["player"]["lastsleep"]
                myp.lastpoo = data["player"]["lastpoo"]
                myp.lastpee = data["player"]["lastpee"]
                myp.lastcum = data["player"]["lastcum"]
                myp.days = data["player"]["days"]
                myp.hunger = data["player"]["hunger"]
                myp.thirst = data["player"]["thirst"]
                mapd = data["map"]
                print("Game loaded successfully!")
                printn(
                    f"""
HERE IS AN OVERVIEW OF YOUR STATS:\n
Name: {myp.name}
Species: {myp.species}
Health: {myp.health}
Weight: {myp.weight}
Defense: {myp.defense}
Height: {myp.height}
Cleanliness: {myp.clean}
Filthiness: {myp.filth}
Speed: {myp.speed}
Attack: {myp.attack}
Lust: {myp.lust}
Armor: {myp.armor}
Inventory: {myp.inventory}
Location: {myp.location}
Status Effects: {myp.status_effects}
Health Issues: {myp.health_issues}
Sizes: {myp.sizes}
Quests: {myp.quests}
Gold: {myp.gold}
Level: {myp.level}

"""
                )

                printn("Welcome back to the game, " + myp.name + "!\n")
                printn("You are currently in " + mapd[myp.location]["name"] + ".\n")
                printn(mapd[myp.location]["description"])

            except Exception as e:
                print("Error loading game: " + str(e))
                exit()

            input("\nPress enter to continue...")
            maingameloop()


def helps():
    print(
        """
[bold magenta]Welcome to the Help Menu![/bold magenta]
[bold magenta]Here you can find all the commands you need to play the game![/bold magenta]
[bold magenta]If you want to go back to the main menu, type 'back'[/bold magenta]
[bold magenta]If you want to go back to the game, type 'game'[/bold magenta]
[bold magenta]If you want to exit the game, type 'exit'[/bold magenta]
[bold magenta]If you want to save the game, type 'save'[/bold magenta]
[bold magenta]If you want to load the game, type 'load'[/bold magenta]
[bold magenta]If you want to see your stats, type 'stats'[/bold magenta]
[bold magenta]If you want to see your inventory, type 'inventory'[/bold magenta]
[bold magenta]If you want to see your quests, type 'quests'[/bold magenta]
"""
    )
    choice = Prompt.ask("What do you want to do?", choices=["back"])
    if choice == "back":
        return


def start_game():
    print(
        "Welcome to the Text Adventure [bold magenta]'The Furry Adventure'[/bold magenta]"
    )
    printn("you can now choose which Character you want to play as\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Characters", justify="center", style="cyan", no_wrap=True)
    table.add_row("1. [bold red]Wolf[/bold red]")
    table.add_row("2. [bold red]Lion[/bold red]")
    table.add_row("3. [bold red]Tiger[/bold red]")
    table.add_row("4. [bold red]Bear[/bold red]")
    table.add_row("5. [bold red]Fox[/bold red]")
    table.add_row("6. [bold red]Custom Character[/bold red]")
    print(table)
    choice = Prompt.ask(
        "What do you want to do?", choices=["1", "2", "3", "4", "5", "6"]
    )
    if choice == "1":
        myp.species = "wolf"
    if choice == "2":
        myp.species = "lion"
    if choice == "3":
        myp.species = "tiger"
    if choice == "4":
        myp.species = "bear"
    if choice == "5":
        myp.species = "fox"
    if choice == "6":
        myp.species = "custom"
        custom()
    print(
        "you have chosen the [bold red]"
        + myp.species
        + "[/bold red] as your Character\n"
    )

    ##NAME##
    printn("Now what is your name\n")
    while True:
        myp.name = Prompt.ask("What is your name?")
        ##check if right
        printn("Are you sure you want to be called " + myp.name + "?\n")

        choice = Prompt.ask("Are you sure?", choices=["yes", "no"])
        if choice == "yes":
            printn("Alright then, let's continue!\n")
            break
        elif choice == "no":
            continue

    printn("Hello " + myp.name + "!\n")
    # stats
    printn("Your stats are:\n")
    calcstats()
    ##rich table
    """
    STATS
        self.name = ""
        self.health = 150
        self.weight = 360
        self.defense = 100
        self.clean = 20
        self.speed = 0
        self.attack = 0
        self.lust = 0
        self.species = ""
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Stats", justify="center", style="cyan", no_wrap=True)
    table.add_row("Health: " + str(myp.health))
    table.add_row("Weight: " + str(myp.weight))
    table.add_row("Defense: " + str(myp.defense))
    table.add_row("Clean: " + str(myp.clean))
    table.add_row("Speed: " + str(myp.speed))
    table.add_row("Attack: " + str(myp.attack))
    table.add_row("Lust: " + str(myp.lust))
    print(table)
    printn("You are now ready to start your adventure!\n")
    os.system("pause")
    maingameloop()


def custom():
    printn("Now you can customize your Character\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Customize", justify="center", style="cyan", no_wrap=True)
    table.add_row("1. [bold red]Name[/bold red]")
    table.add_row("2. [bold red]Health[/bold red]")
    table.add_row("3. [bold red]Weight[/bold red]")
    table.add_row("4. [bold red]Defense[/bold red]")
    table.add_row("5. [bold red]Clean[/bold red]")
    table.add_row("6. [bold red]Speed[/bold red]")
    table.add_row("7. [bold red]Attack[/bold red]")
    table.add_row("8. [bold red]Lust[/bold red]")
    print(table)
    choice = Prompt.ask(
        "What do you want to do?", choices=["1", "2", "3", "4", "5", "6", "7", "8"]
    )
    if choice == "1":
        myp.name = Prompt.ask("What is your name?")
    if choice == "2":
        myp.health = int(Prompt.ask("How much health do you want?"))
    if choice == "3":
        myp.weight = Prompt.ask("How much weight do you want?")
    if choice == "4":
        myp.defense = Prompt.ask("How much defense do you want?")
    if choice == "5":
        myp.clean = int(Prompt.ask("How much clean do you want?"))
    if choice == "6":
        myp.speed = Prompt.ask("How much speed do you want?")
    if choice == "7":
        myp.attack = Prompt.ask("How much attack do you want?")
    if choice == "8":
        myp.lust = Prompt.ask("How much lust do you want?")
    print(
        "you have chosen the [bold red]"
        + myp.species
        + "[/bold red] as your Character\n"
    )
    return


def maingameloop():
    # print(mapd)
    while myp.health > 0:
        os.system("cls")
        calcstats()
        ##print table with location details
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Location", justify="center", style="cyan", no_wrap=True)
        table.add_row("Name: " + mapd[myp.location]["name"])
        table.add_row("Description: " + mapd[myp.location]["description"])
        if mapd[myp.location]["looked"]:
            if mapd[myp.location]["enemies"] != []:
                table.add_row(
                    "Enemies: "
                    + str(mapd[myp.location]["enemies"])
                    .replace("[", "")
                    .replace("]", "")
                    .replace("'", "")
                )
        if mapd[myp.location]["items"] != {}:
            table.add_row("Items: " + str(mapd[myp.location]["items"]))
        if mapd[myp.location]["NPC"] != []:
            table.add_row(
                "NPCs: "
                + str(mapd[myp.location]["NPC"])
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
            )
        # add exists
        if mapd[myp.location]["exits"]["north"] != []:
            temp = mapd[myp.location]["exits"]["north"]
            table.add_row("North: " + mapd[temp]["name"])
        if mapd[myp.location]["exits"]["south"] != []:
            temp = mapd[myp.location]["exits"]["south"]
            table.add_row("South: " + mapd[temp]["name"])
        if mapd[myp.location]["exits"]["east"] != []:
            temp = mapd[myp.location]["exits"]["east"]
            table.add_row("East: " + mapd[temp]["name"])
        if mapd[myp.location]["exits"]["west"] != []:
            temp = mapd[myp.location]["exits"]["west"]
            table.add_row("West: " + mapd[temp]["name"])

        print(table)
        idletext()
        if myp.lust > 70:
            lustinf()
        if myp.filth > 70:
            dirtyinf()
        # ask for prompt move look etc
        choice = Prompt.ask(
            "\nWhat do you want to do?",
            choices=[
                "move",
                "look",
                "talk",
                "take",
                "appearence",
                "stats",
                "inventory",
                "exit",
                "save",
            ],
        )
        try:
            if choice == "appearence":
                printn(getappearence(), 0.5)
                os.system("pause")
            if choice == "move":
                move()
            if choice == "look":
                look()
            if choice == "stats":
                stats()

            if choice == "inventory":
                inventory()
            if choice == "exit":
                exit()
            if choice == "save":
                save(mapd)
            if choice == "take":
                take()

            if choice == "talk":
                if mapd[myp.location]["NPC"] == []:
                    printn("There is no one to talk to\n")
                    time.sleep(1)
                    continue
                from utils.NPC_action import talkNPC

                printn("Who do you want to talk to?\n")
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("Talk", justify="center", style="cyan", no_wrap=True)
                if mapd[myp.location]["NPC"] != []:
                    for i in mapd[myp.location]["NPC"]:
                        table.add_row(i)
                print(table)
                choice = Prompt.ask(
                    "Who do you want to talk to?", choices=mapd[myp.location]["NPC"]
                )
                talkNPC(choice)
        except Exception as error:
            ##print error
            printn("Error: " + str(error) + "\n")
            os.system("pause")
            pass


def move():
    printn("Where do you want to go?\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Move", justify="center", style="cyan", no_wrap=True)
    if mapd[myp.location]["exits"]["north"] != []:
        temp = mapd[myp.location]["exits"]["north"]
        table.add_row("North: " + mapd[temp]["name"])
    if mapd[myp.location]["exits"]["south"] != []:
        temp = mapd[myp.location]["exits"]["south"]
        table.add_row("South: " + mapd[temp]["name"])
    if mapd[myp.location]["exits"]["east"] != []:
        temp = mapd[myp.location]["exits"]["east"]
        table.add_row("East: " + mapd[temp]["name"])
    if mapd[myp.location]["exits"]["west"] != []:
        temp = mapd[myp.location]["exits"]["west"]
        table.add_row("West: " + mapd[temp]["name"])
    print(table)
    choice = input("Where do you want to go?\n").lower()
    if choice in ["n", "north"]:
        if mapd[myp.location]["exits"]["north"] != []:
            myp.location = mapd[myp.location]["exits"]["north"]
            printn("You have moved North\n")
        else:
            printn("You cannot go North\n")
    if choice in ["s", "south"]:
        if mapd[myp.location]["exits"]["south"] != []:
            myp.location = mapd[myp.location]["exits"]["south"]
            printn("You have moved South\n")
        else:
            printn("You cannot go South\n")
    if choice in ["e", "east"]:
        if mapd[myp.location]["exits"]["east"] != []:
            myp.location = mapd[myp.location]["exits"]["east"]
            printn("You have moved East\n")
        else:
            printn("You cannot go East\n")
    if choice in ["w", "west"]:
        if mapd[myp.location]["exits"]["west"] != []:
            myp.location = mapd[myp.location]["exits"]["west"]
            printn("You have moved West\n")
        else:
            printn("You cannot go West\n")
    time.sleep(1)
    return


def look():
    printn("you look around\n")
    printn(mapd[myp.location]["description"] + "\n")
    if mapd[myp.location]["enemies"] != []:
        mapd[myp.location]["looked"] = True
        enemies = mapd[myp.location]["enemies"]
        printn("You see the following enemies:\n")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Enemy", justify="center", style="cyan", no_wrap=True)
        for i in enemies:
            table.add_row(i)
        print(table)
    if mapd[myp.location]["NPC"] != []:
        printn("You see the following people:\n")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("NPC", justify="center", style="cyan", no_wrap=True)
        for i in mapd[myp.location]["NPC"]:
            table.add_row(i)
        print(table)
    if mapd[myp.location]["items"] != []:
        printn("You see the following items:\n")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Item", justify="center", style="cyan", no_wrap=True)
        for i in mapd[myp.location]["items"]:
            table.add_row(i)
        print(table)
    time.sleep(3)


def take():
    # panel
    printn("What do you want to take?\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Item", justify="center", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="center", style="purple", no_wrap=True)
    table.add_column("Type", justify="center", style="yellow", no_wrap=True)
    if mapd[myp.location]["items"] != []:
        for i in mapd[myp.location]["items"]:
            type = gettypeofitem(i)
            table.add_row(i, str(mapd[myp.location]["items"][i]), type)
    print(table)
    choice = Prompt.ask(
        "What do you want to take?", choices=mapd[myp.location]["items"]
    )
    if choice in mapd[myp.location]["items"]:
        if choice not in myp.inventory:
            myp.inventory[choice] = 1
        else:
            myp.inventory[choice] += 1

        # "items": {
        #   "weight gain potion": 3
        # },
        # remove only one of the item
        mapd[myp.location]["items"][choice] -= 1
        if mapd[myp.location]["items"][choice] == 0:
            mapd[myp.location]["items"].pop(choice)

        print("You have taken [red]" + choice + "[/red]\n")
        time.sleep(1)


def inventory():
    printn("You have the following items:\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Item", justify="center", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="center", style="purple", no_wrap=True)
    table.add_column("Type", justify="center", style="yellow", no_wrap=True)
    for i in myp.inventory:
        table.add_row(i, str(myp.inventory[i]), gettypeofitem(i))
    print(table)
    choice = Prompt.ask("What do you want to do?", choices=["use", "drop", "back"])
    if choice == "use":
        use()
    if choice == "drop":
        drop()
    if choice == "back":
        return


def use():
    # panel
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Item", justify="center", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="center", style="purple", no_wrap=True)
    table.add_column("Type", justify="center", style="yellow", no_wrap=True)
    for i in myp.inventory:
        type = gettypeofitem(i)
        table.add_row(i, str(myp.inventory[i]), type)
    print(table)

    choice = Prompt.ask(">", choices=myp.inventory)
    if choice in myp.inventory:
        info = getiteminfo(choice)
        effects = ITEMS[info[0]][info[1]][choice]["effects"]
        for i in effects:
            if str(i).startswith("ADD"):
                i = i[3:]
                if str(i).lower() == "weight":
                    myp.weight = myp.weight + effects["ADD" + i]
                    print(
                        "You have gained [red] [bold]"
                        + str(effects["ADD" + i])
                        + "[/red] [/bold] weight\n"
                    )
                if str(i).lower() == "lust":
                    myp.lust = myp.lust + effects["ADD" + i]
                    print(
                        "You have gained [red bold]"
                        + str(effects["ADD" + i])
                        + "[/red /bold] lust\n"
                    )
                if str(i).lower().startswith("size"):
                    i = i[4:]
                    myp.addedsizes[i] = myp.addedsizes[i] + effects["ADDSIZE" + i]
                    print(
                        "your "
                        + i
                        + " has grown by "
                        + str(effects["ADDSIZE" + i])
                        + "\n"
                    )
            else:
                if str(i).lower() == "hunger":
                    temp = myp.hunger
                    myp.hunger = myp.hunger + effects[i]
                    if myp.hunger < temp:
                        if myp.hunger < 0:
                            myp.hunger = 0
                        print(
                            "your hunger has decreased by [green]"
                            + str(effects[i]).replace("-", "")
                            + "[/green]\n"
                        )
                    else:
                        if myp.hunger > 100:
                            myp.hunger = 100
                        print(
                            "your hunger has increased by [orange]"
                            + str(effects[i]).replace("-", "")
                            + "[/orange]\n"
                        )
                if str(i).lower() == "thirst":
                    temp = myp.thirst
                    myp.thirst = myp.thirst + effects[i]
                    if myp.thirst < temp:
                        if myp.thirst < 0:
                            myp.thirst = 0
                        print(
                            "your thirst has decreased by [green]"
                            + str(effects[i]).replace("-", "")
                            + "[/green]\n"
                        )
                    else:
                        if myp.thirst > 100:
                            myp.thirst = 100
                        print(
                            "your thirst has increased by [orange]"
                            + str(effects[i]).replace("-", "")
                            + "[/orange]\n"
                        )
    time.sleep(5)


def drop():
    printn("You have the following items:\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Item", justify="center", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="center", style="purple", no_wrap=True)
    table.add_column("Type", justify="center", style="yellow", no_wrap=True)
    for i in myp.inventory:
        table.add_row(i, str(myp.inventory[i]), gettypeofitem(i))
    print(table)
    choice = Prompt.ask("What do you want to drop?", choices=myp.inventory)
    if choice in myp.inventory:
        myp.inventory[choice] -= 1
        if myp.inventory[choice] == 0:
            myp.inventory.pop(choice)
        mapd[myp.location]["items"][choice] += 1
        print("You have dropped [red]" + choice + "[/red]\n")
        time.sleep(1)
    else:
        print("You don't have that item\n")
        time.sleep(1)


def stats():
    ##get player stats
    printn("Your stats are:\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Stat", justify="center", style="cyan", no_wrap=True)
    table.add_column("Value", justify="center", style="purple", no_wrap=True)
    table.add_row("Name", myp.name)
    table.add_row("Species", myp.species)
    table.add_row("Height", str(myp.height) + "'")
    table.add_row("Clean", str(myp.clean) + "%")
    # weight and sizes
    table.add_row("Weight", str(myp.weight))
    for i in myp.sizes:
        table.add_row(i, str(myp.normalsizes[i] + myp.addedsizes[i]) + '"')
    # hunger and thirst
    table.add_row("Hunger", str(myp.hunger))
    table.add_row("Thirst", str(myp.thirst))
    # lust
    table.add_row("Lust", str(myp.lust))
    # level and xp
    table.add_row("Level", str(myp.level))
    table.add_row("XP", str(myp.xp))
    # inventory
    table.add_row("Inventory", str(len(myp.inventory)))
    print(table)
    os.system("pause")


# credits
def credits():
    printn("This game was made by: PrOwOtogen\n")
    # game description
    printn(
        """In this game, you play as an anthropomorphic animal on a journey through a magical world. Your goal is to explore the various landscapes, meet new characters, and complete challenges along the way. As you progress, you will earn experience points and level up, allowing you to gain strength, abilities, and size. With each level up, your character will grow larger, becoming more imposing and powerful. The increased size will bring with it a sense of pride and confidence, making you feel unstoppable as you continue on your journey.

However, this growth will also bring with it an insatiable hunger and a desire for indulgence. You will need to carefully balance your actions and make choices that support your weight gain goals, all while avoiding any dangers that may arise. The game will be filled with exciting moments, sensual encounters, and a journey towards ultimate indulgence. Are you ready to embark on a journey of self-discovery and indulgence? Then come play this thrilling text adventure game!"""
    )


def startup():
    global mapd
    global ITEMS
    print("Starting up...")
    try:
        mapd = getmap()
        ITEMS = getitems()
    except Exception as error:
        print("Error: " + str(error))
        print("Please report this error to the developer.")
        os.system("pause")
        exit()

    print("mapd: " + str(mapd))
    print("ITEMS: " + str(ITEMS))
    print("Startup complete!")
    os.system("cls")


if __name__ == "__main__":
    main_menu()
