from math import floor
import random
from tkinter import N
from ent import *
import os
import sys
from rich import print
import logging
from rich.logging import RichHandler
import time
from rich.console import Console
from rich.table import Table
from rich.table import Column
# import rich progress bar
from rich.progress import Progress, BarColumn, TextColumn
import json

sys.path.append(".")
os.system("cls")

NAME_TOM = {}


nameoftxta = "[green][blink]Hey[/blink][/green]"


# import from ent
eny = enemy()
myp = Player()

# other words for commands
invent = ["inventory", "inv", "i"]
examines = ["examine"]
looks = ["look", "l"]
up = ["up", "north", "n", "u"]
down = ["down", "south", "s", "d"]
right = ["right", "r", "east", "e"]
left = ["left", "l", "west", "w"]
grab = ["grab", "take", "get"]

# other vars


def impo_js(js):
    print(f"importing {js} JSON")

    #
    if js == "NPCs":
        with open("jsons/Characters.json", "r") as f:
            data = json.load(f)
            return data
    elif js == "rands":
        with open("jsons/actions.json", "r") as f:
            data = json.load(f)

    return data


myp.enemymult = 0
myp.playermult = 0
NPCs = impo_js("NPCs")
rands = impo_js("rands")

# map

MAP = {
    "a1": {
        "name": "Bedroom",
        "desc": "This is your Bedroom,",
        "isexamined": False,
        "items": {"food": 1,
                  "book": 1,
                  "key": 2},
        "enemy": "none",
        "isfought": False,
        "UP": "a1",
        "DOWN": "b1",
        "LEFT": "a1",
        "RIGHT": "a2"
    },
    "a2": {
        "name": "hallway",
        "desc": "a Hallway, nothing special",
        "isexamined": False,
        "examine": "theres an Enemy",
        "items": {},
        "enemy": ["bandit", "orc"],
        "isfought": False,
        "UP": "a2",
        "DOWN": "b2",
        "LEFT": "a1",
        "RIGHT": "a3"
    }
}


def start():
    # importing JSONS
    print(
        f"Welcome to my Textadventure '{nameoftxta}'\nI hope you have a great time and let´s start with the Charactergeneration\n[center]If you don´t have any questions, press [green][bold]1[/bold][/green]. \nFor commands [yellow][bold]2[/yellow][/bold]\nTo [red][blink]exit[/blink] 3")
    i = input("INP: ").lower().strip()

    if i == "1":
        chargen()
    elif i == "2":
        helps()
    elif i == "3":
        os.system("exit")
    elif i == "4":
        maingameloop()


def chargen():
    myp.loc = "a1"
    os.system("cls")
    print(
        "Now we´re at the point where you can create your [blink]Character[/blink]\nWhich Name do you want to choose?\nINP: ")
    myp.name = input()
    print(f"Do you want:[orange]{myp.name}[/orange] for your name?")
    i = input("INP: ").lower().strip()
    if i == "yes":
        myp.name = myp.name
    elif i == "no":
        print("[red]What´s your name?[/red]")
        myp.name = input()
    sel_role()


def sel_role():
    # select role
    roles = ["warrior", "mage", "thief"]
    print(
        "choose between [green]warrior[/green], [yellow]mage[/yellow] or [cyan]thief[/cyan]")
    i = input("INP: ").lower().strip()
    if i == "warrior":
        myp.role = "warrior"
    elif i == "mage":
        myp.role = "mage"
    elif i == "thief":
        myp.role = "thief"
    else:
        print("[red]invalid input[/red]")
        sel_role()
    if myp.role == "warrior":
        myp.hp = 100
        myp.maxhp = myp.hp
        myp.atk = randint(5, 8)
        myp.defence = randint(1, 3)
        myp.weight = randint(90, 130)
    elif myp.role == "mage":
        myp.hp = 100
        myp.maxhp = myp.hp
        myp.atk = randint(3, 5)
        myp.defence = randint(2, 3)
        myp.weight = randint(70, 100)
    elif myp.role == "thief":
        myp.hp = 100
        myp.maxhp = myp.hp
        myp.atk = randint(3, 5)
        myp.defence = randint(2, 3)
        myp.weight = randint(60, 100)
    print(f"Your [orange]{myp.role}[/orange] is ready!")
    print(f"Your [orange]{myp.role}[/orange] has [orange]{myp.hp}[/orange] HP\n[orange]{myp.atk}[/orange] ATK\n[orange]{myp.defence}[/orange] DEF\n[orange]{myp.weight}[/orange] WEIGHT")
    myp.inv = {}
    time.sleep(2)
    sel_diff()

# difficulty


def sel_diff():
    os.system("cls")
    print(
        "choose between [green]easy[/green], [yellow]normal[/yellow] or [cyan]hard[/cyan]")
    i = input("INP: ").lower().strip()
    if i == "easy":
        myp.diff = "easy"
    elif i == "normal":
        myp.diff = "normal"
    elif i == "hard":
        myp.diff = "hard"
    else:
        print("[red]invalid input[/red]")
        sel_diff()

    print(f"You chose [orange]{myp.diff}[/orange]")
    print("[green]You are ready to start the game![/green]")

    if myp.diff == "easy":
        myp.enemymult = 0.7
        myp.playermult = 1.5
    elif myp.diff == "normal":
        myp.enemymult = 1
        myp.playermult = 1.1
    elif myp.diff == "hard":
        myp.enemymult = 1.3
        myp.playermult = 0.9
    else:
        myp.enemymult = 1
        myp.playermult = 1
    # print difficulty
    print(
        f"[red]Enemydemage multiplier: {myp.enemymult}[/red] the Player Multiplier: [orange]{myp.playermult}[/orange]")
    time.sleep(2)
    maingameloop()


def helps():
    os.system("cls")
    print("HELP:")
    print(
        "to move use [green]up[/green], [yellow]down[/yellow], [cyan]left[/cyan] or [red]right[/red]")
    print("to examine use [green]examine[/green]")
    print("to look around use [green]look[/green]")
    print("to go back to the main menu use [green]menu[/green]")
    i = input("INP: ").lower().strip()
    if i == "menu":
        start()
    else:
        helps()


def maingameloop():
    while myp.hp > 0:
        os.system("cls")
        # create rich table
        print("you are at: [green]{}[/green]".format(myp.loc))
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Command", style="bold green")
        table.add_column("Description", style="bold yellow")
        # add row(name)
        table.add_row("[yellow blink]Gold[/yellow blink]",
                      f"[yellow blink]{myp.gold}[/yellow blink]")
        table.add_row(
            "Name",  f"[red blink]{MAP[myp.loc]['name']}[/red blink]")
        table.add_row("look", look())
        table.add_row("up", "go up")
        table.add_row("down", "go down")
        table.add_row("left", "go left")
        table.add_row("right", "go right")
        table.add_row("grab", "grab an item")
        if MAP[myp.loc]["isexamined"] == False:
            table.add_row("examine", "examine")
        else:
            c = 0
            t = "There is: "
            for i in MAP[myp.loc]['items']:
                # print out the value of item
                t += f"[green]{MAP[myp.loc]['items'][i]}[/green] [red]{i}[/red][purple],[/purple] "
                c += 1
            table.add_row("examine", f"{t}")
        # show table
        print(table)

        # print hp
        txt = check_randomactions()
        print(txt)
        print(
            f"Your [orange]{myp.role}[/orange] has [orange]{myp.hp}[/orange] HP")
        print("0 ", end="")
        for i in range(myp.hp):
            print("[green]█[/green]", end="")
        for i in range(myp.maxhp - myp.hp):
            print("[red]░[/red]", end="")
        print(f" {myp.maxhp}")
        for i in range(myp.hp):
            print(" ", end="")
        print(str(myp.hp))

        # print out random actions
        print("#" * 50)

        i = input("INP: ").lower().strip()
        if i in up:
            move("UP")
        elif i in down:
            move("DOWN")
        elif i in left:
            move("LEFT")
        elif i in right:
            move("RIGHT")
        elif i in examines:
            examine()
        elif i in grab:
            grab_item()
        elif i in invent:
            if myp.inv == []:
                print("you don´t have any items")
                time.sleep(2)
            else:
                inv()
        else:
            maingameloop()
    print("[red]You died![/red]")
    # want to restart?
    i = input("INP: ").lower().strip()
    if i == "yes":
        start()
    else:
        os.system("exit")


def inv():
    os.system("cls")
    print("Your inventory:")
    # table for inventory items and description
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Count", style="bold green")
    table.add_column("Item", style="bold yellow")
    # add row(name)
    inve = []
    c = 0
    # create a row for each item with number and name

    for i in myp.inv:
        table.add_row(str(myp.inv[i]), str(i))
        c += 1
    # show table
    print(myp.inv)
    print(table)
    print("[green]menu[/green] Back to [green]menu[/green]")
    print("[green]Item Name[/green] to use item")
    i = input("INP: ").lower().strip()
    if i == "menu":
        maingameloop()
    elif i in myp.inv:
        use(i)
    elif i == "menu":
        maingameloop()
    else:
        inv()

# grab item


def grab_item():
    # you can grab
    os.system("cls")
    if MAP[myp.loc]["items"] != []:
        c = 0
        t = "you can grab: "
        item = []
        for i in MAP[myp.loc]['items']:
            # print out the value of item
            t += f"[green]{MAP[myp.loc]['items'][i]}[/green] [red]{i}[/red][purple] or[/purple] "
            c += 1
            item += [i]
        print(t)
        print(item)
        i = input().lower().strip()
        if i in item:
            print(myp.inv)
            # add item to inventory with count
            # add item to inventory
            Icount = 1
            for a in myp.inv:
                if a == i:
                    Icount += 1
            upd = {f"{i}": Icount}
            myp.inv.update(upd)

            c = 0

            # remove one item from map
            MAP[myp.loc]['items'][i] -= 1
            # remove item from map if 0
            if MAP[myp.loc]['items'][i] == 0:
                del MAP[myp.loc]['items'][i]
            # display the item that is being grabbed
            print(f"[green]You grabbed: {i}[/green]")
            # timer to wait 2 seconds
            time.sleep(2)
            maingameloop()
        else:
            print(f"[red]You can't grab that![/red]")
            # timer to wait 2 seconds
            time.sleep(2)
            grab_item()
    else:
        print("There is nothing to grab!")
        # timer to wait 2 seconds
        time.sleep(2)
        maingameloop()


def use(i):
    os.system("cls")
    print(f"You use [orange]{i}[/orange]")
    if i == "potion":
        myp.hp += 10
        if myp.hp > myp.maxhp:
            myp.hp = myp.maxhp
        print(f"You have [green]{myp.hp}[/green] HP")

        time.sleep(2)
        removeItem(i)
        maingameloop()

    elif i == "sword":
        myp.atk += 5
        print(f"You have [green]{myp.atk}[/green] ATK")
        time.sleep(2)
        removeItem(i)
        maingameloop()
    elif i == "shield":
        myp.defence += 5
        print(f"You have [green]{myp.defence}[/green] DEF")
        time.sleep(2)
        removeItem(i)
        maingameloop()
    elif i == "food":
        myp.hp += 20
        myp.weight += 20
        if myp.hp > myp.maxhp:
            myp.hp = myp.maxhp
        print(
            f"You have [green]{myp.hp}[/green] HP\nYou [red]gained 20 lbs[/red] and you´re now at [green]{myp.weight}[/green] lbs")
        time.sleep(2)
        removeItem(i)
        maingameloop()
    elif i == "key":
        print("You found a key!")
        time.sleep(2)
        removeItem(i)
        maingameloop()

    else:
        print("[red]You can´t use this item[/red]")
        time.sleep(2)
        inv()


def removeItem(i):
    myp.inv[f"{i}"] -= 1
    if myp.inv[f"{i}"] == 0:
        del myp.inv[f"{i}"]
    maingameloop()


def move(direction):
    if direction in MAP[myp.loc]:
        myp.loc = MAP[myp.loc][direction]
        maingameloop()
    else:
        print("[red]You can´t go that way[/red]")
        maingameloop()


def examine():
    os.system("cls")
    if MAP[myp.loc]["enemy"] != "none":
        print(
            "There is an enemy here!\nDo you want to [green]fight[/green] or [green]run[/green]?")
        i = input("INP: ").lower().strip()
        if i == "fight":
            fightgen()
        elif i == "run":
            print("You ran away!")
            time.sleep(2)
            maingameloop()
        else:
            print("[red]You can´t do that![/red]")
            time.sleep(2)
            examine()
        # timer to wait 2 seconds
    else:
        c = 0
        if MAP[myp.loc]["items"] == {}:
            print("There is nothing here")
        else:
            t = "There is: "
            MAP[myp.loc]["isexamined"] = True
            for i in MAP[myp.loc]['items']:
                # print out the value of item
                t += f"[green]{MAP[myp.loc]['items'][i]}[/green] [red]{i}[/red][purple],[/purple] "
                c += 1
            print(t)
            # check for enemy
        time.sleep(2)
        maingameloop()


def look():
    return f"you can see: [green]{MAP[myp.loc]['desc']}[/green]"


def fightgen():
    # generate a random enemy
    enemy = random.choice(MAP[myp.loc]["enemy"])
    if enemy == "goblin":
        eny.name = "Goblin"
        eny.hp = random.randint(10, 20)
        eny.maxhp = eny.hp
        eny.atk = random.randint(1, 5)
        eny.gold = random.randint(1, 5)
    elif enemy == "orc":
        eny.name = "Orc"
        eny.hp = random.randint(20, 30)
        eny.maxhp = eny.hp
        eny.atk = random.randint(5, 10)
        eny.gold = random.randint(5, 10)
    elif enemy == "skeleton":
        eny.name = "Skeleton"
        eny.hp = random.randint(30, 40)
        eny.maxhp = eny.hp
        eny.atk = random.randint(10, 15)
        eny.gold = random.randint(10, 15)
    elif enemy == "dragon":
        eny.name = "Dragon"
        eny.hp = random.randint(40, 50)
        eny.maxhp = eny.hp
        eny.atk = random.randint(15, 20)
        eny.gold = random.randint(15, 20)
    elif enemy == "boss":
        eny.name = "Boss"
        eny.hp = random.randint(50, 60)
        eny.maxhp = eny.hp
        eny.atk = random.randint(20, 25)
        eny.gold = random.randint(20, 25)
    elif enemy == "bandit":
        eny.name = "Bandit"
        eny.lvl = random.randint(5, 30)
        eny.hp = random.randint(10, 25)
        eny.maxhp = eny.hp
        eny.atk = random.randint(1, 10)
        eny.gold = random.randint(1, 25)
    fightloop()


def fightloop():
    # fight loop
    while myp.hp > 0 and eny.hp > 0:
        # floor myp.hp
        myp.hp = floor(myp.hp)
        eny.hp = floor(eny.hp)
        os.system("cls")
        # printHP
        print(
            f"Your [orange]{myp.role}[/orange] has [orange]{myp.hp}[/orange] HP")
        print("0 ", end="")
        for i in range(myp.hp):
            print("[green]█[/green]", end="")
        for i in range(myp.maxhp - myp.hp):
            print("[red]░[/red]", end="")
        print(f" {myp.maxhp}")
        for i in range(myp.hp):
            print(" ", end="")
        print(str(myp.hp))
        # print enyHP
        print(f"The {eny.name} has [orange]{eny.hp}[/orange] HP")
        print("0 ", end="")
        for i in range(eny.hp):
            print("[orange]█[/orange]", end="")
        for i in range(eny.maxhp - eny.hp):
            print("[red]░[/red]", end="")
        print(f" {eny.maxhp}")
        for i in range(eny.hp):
            print(" ", end="")
        print(str(eny.hp))

        # player attacks
        playeratk = calc_dmg()
        eny.hp -= playeratk
        print(
            f"you attacked the {eny.name} for [green]{playeratk}[/green] damage")
        time.sleep(2)
        # check if enemy is dead
        if eny.hp <= 0:
            print(f"you killed the {eny.name}")
            time.sleep(2)
            gold = cal_getGold(eny.gold)
            myp.gold += gold
            cal_xp()
            print(f"you gained [green]{gold}[/green] gold")
            time.sleep(2)
            MAP[myp.loc]["enemy"] = "none"
            maingameloop()
        # enemy attacks
        enymatk = cal_enydmg()
        myp.hp -= enymatk

        print(
            f"the {eny.name} attacked you for [green]{enymatk}[/green] damage")
        time.sleep(2)
        # check if enemy is dead
        # check if player is dead
        if myp.hp <= 0:
            print(f"you died")
            time.sleep(2)
            maingameloop()


def calc_dmg():
    # calculate damage
    dmg = myp.atk + ((myp.lvl*myp.playermult) / myp.atk * random.randint(1, 5))
    return dmg


def cal_getGold(eny):
    # calculate gold
    gold = eny * myp.playermult
    # round gold
    gold = round(gold)
    return gold


def cal_xp():
    # calculate xp
    xp = eny.xp + ((myp.lvl*myp.playermult) / random.randint(1, 5))
    while xp >= 100:
        myp.lvl += 1
        print(f"you leveled up to [green]{myp.lvl}[/green]")
        time.sleep(2)
        xp -= 100
    return


def cal_enydmg():
    # calculate damage
    dmg = eny.atk + ((eny.lvl*myp.enemymult) / eny.atk *
                     random.randint(1, 5)) - myp.defence
    if dmg < 0:
        eny.damage += 1
        cal_enydmg()
    return dmg


def check_randomactions():
# 1 - weight
# 2 - lust
# 7 - loc
    typ = random.randint(1,20)
    # print(rands["actions"]['a1']['none']['text']["w<130"])
    a_w_idle = rands["actions"]["idle"]
    a_idle = rands["actions"][myp.loc]["idle"]
    if myp.loc in rands["actions"]:

        
        if typ == 1:
            #weight
            if myp.weight < 130:

                ret = random.choice(a_w_idle["text"]["w>130"])
            elif myp.weight >=130 and myp.weight < 200:
                ret = random.choice(a_w_idle["text"]["w<130"])
        elif typ == 2:
        #lust
            return
        elif typ == 7:
            #loc
            if myp.weight < 130:
                ret = random.choice(a_idle["text"]["w<130"])
            elif myp.weight >=130 and myp.weight < 200:
                ret = random.choice(a_idle["text"]["w>130"])
        

    return ret


start()
