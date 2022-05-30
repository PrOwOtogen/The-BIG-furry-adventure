from math import floor
import random
import os
import sys
from rich import print
from rich.logging import RichHandler
import time
from rich.console import Console
from rich.table import Table
from rich.table import Column
# import rich progress bar
from rich.progress import Progress, BarColumn, TextColumn
import json


# import python files
from npc_action import smalltalk
from ent import *
from map import MAP
from calculations import *
from randomac import check_randomactions


sys.path.append(".")
os.system("cls")

NAME_TOM = {}


nameoftxta = "[green][blink]The [italic bold]BIG[/italic bold] Furry Adventure[/blink][/green]"


# NPCs
a_m = alex()


# import from ent
eny = enemy()
myp = Player()
globitem = globitems

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
        myp.hp = round(myp.hp)
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
        txt = check_randomactions()
        print(txt)

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
        if MAP[myp.loc][direction] == myp.loc:
            print("[red]You can´t go that way![/red]")
            time.sleep(1)
        myp.loc = MAP[myp.loc][direction]
        maingameloop()
    else:
        print("[red]You can´t go that way[/red]")
        maingameloop()


def examine():
    os.system("cls")
    if MAP[myp.loc]["enemy"] != "none" and not MAP[myp.loc]["enemy"] == "NPC":
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
    elif MAP[myp.loc]["enemy"] == "NPC":
        print("There is an NPC here!")
        print("Do you want to [green]talk[/green] or [green]not[/green]?")
        i = input("INP: ").lower().strip()
        if i == "talk":
            NPC()
        elif i == "not":
            print("You didn´t talk to the NPC")
            time.sleep(2)
            maingameloop()
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
            eny.name = "enemy"
            eny.hp = 0
            eny.maxhp = 0
            eny.damage = 0
            eny.xp = 0
            eny.lvl = 1
            eny.gold = 0
            maingameloop()
        # enemy attacks
        enymatk = cal_enydmg()
        myp.hp -= enymatk

        print(
            f"the {eny.name} attacked you for [green]{enymatk}[/green] damage")
        time.sleep(2)
        # set every var from eny to 0

        # check if enemy is dead
        # check if player is dead
        if myp.hp <= 0:
            print(f"you died")
            time.sleep(2)
            eny.name = "enemy"
            eny.hp = 0
            eny.maxhp = 0
            eny.damage = 0
            eny.xp = 0
            eny.lvl = 1
            eny.gold = 0
            maingameloop()


def NPC():
    if MAP[myp.loc]["NPC"] == "alex_the_merchant":
        tradewithAlex()
    else:
        print("No NPC here")
        time.sleep(2)
    maingameloop()


def smoothwrite(text, speed):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    return


# NPC ACTIONS
def tradewithAlex():
    if myp.weight < 130:
        text = NPCs["Alex_the_merchant"]["Greeting"]["w<130"]
    elif myp.weight > 130 and myp.weight < 200:
        text = NPCs["Alex_the_merchant"]["Greeting"]["w130-200"]
    elif myp.weight > 200:
        text = NPCs["Alex_the_merchant"]["Greeting"]["w>200"]
    text = text.replace("<name>", myp.name)
    smoothwrite(text, 0.05)
    time.sleep(1)
    print("\n[yellow]trade\n[green]smalltalk\n[red]leave")
    i = input(">").lower().strip()
    if i in ["trade", "t"]:
        trade()
    elif i in ["smalltalk", "s"]:
        smalltalk("Alex")
    elif i == "leave":
        maingameloop()
    else:
        print("[red]I don't understand")
        time.sleep(1)
        tradewithAlex()


def trade():
    print("[yellow]What do you want to do?")
    print("[green]Buy items\n[red]Sell Items\n[blue]Leave")
    i = input(">").lower().strip()
    if i in ["buy", "b"]:
        tradebuy()
    elif i in ["sell", "s"]:
        tradesell()
    elif i in ["leave", "l"]:
        maingameloop()
    else:
        print("[red]I don't understand")
        time.sleep(1)
        trade()


def tradebuy():
    buymult = 1
    # check for money
    if myp.gold == 0:
        print("[red]You don't have any gold")
        time.sleep(1)
        trade()
    if a_m.love < 20:
        buymult = 1.5
    elif a_m.love > 20 and a_m.love < 40:
        buymult = 1.25
    elif a_m.love > 40 and a_m.love < 60:
        buymult = 1
    elif a_m.love > 60 and a_m.love < 80:
        buymult = 0.75
    elif a_m.love > 80:
        buymult = 0.5
    smoothwrite("[yellow]What do you want to buy?\n", 0.05)
    items = {"sword": round(12/buymult), "shield": round(10/buymult),
             "armor": round(10/buymult), "potion": round(5/buymult)}
    a_m.inventory.update(items)
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Item", style="bold green")
    table.add_column("price", style="bold yellow")
    for i in a_m.inventory:
        # create a rich table with item and price
        table.add_row(str(i), str(a_m.inventory[i]))
    print(table)
    time.sleep(1)
    buy = input("I want to buy: ").lower().strip()

    if buy in a_m.inventory:
        if myp.gold >= a_m.inventory[buy]:
            myp.gold -= a_m.inventory[buy]
            Icount = 1
            for a in myp.inv:
                if a == buy:
                    Icount += 1
            upd = {f"{buy}": Icount}
            myp.inv.update(upd)
            print("[green]You bought {} for {} gold".format(
                buy, a_m.inventory[buy]))
            time.sleep(1)
        else:
            print("[red]You don't have enough gold")
            time.sleep(1)


def tradesell():
    sellmult = 1

    if a_m.love < 20:
        sellmult = 0.5
    elif a_m.love > 20 and a_m.love < 40:
        sellmult = 0.75
    elif a_m.love > 40 and a_m.love < 60:
        sellmult = 1
    elif a_m.love > 60 and a_m.love < 80:
        sellmult = 1.25
    elif a_m.love > 80:
        sellmult = 1.5
    smoothwrite("What do you want to sell?\n", 0.05)
    # make a table of items and prices
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Item", style="bold green")
    table.add_column("price", style="bold yellow")
    for i in myp.inv:
        if i in globitem:
            table.add_row(str(i), str(round(globitem[i]*sellmult)))
    print(table)
    time.sleep(1)
    sell = input("I want to sell: ").lower().strip()
    if sell in myp.inv and sell in globitem:
        myp.gold += round(globitem[sell]*sellmult)
        myp.inv[sell] -= 1
        if myp.inv[sell] == 0:
            del myp.inv[sell]
        print("[green]You sold {} for {} gold".format(
            sell, round(globitem[sell]*sellmult)))


start()
