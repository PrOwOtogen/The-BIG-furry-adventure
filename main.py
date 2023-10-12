import rich
import time
import sys

from characters.player import *
from engine.printn import *
from engine.conversion import *


def mainmenu():
    printn(
        "Welcome to TBFA (The Big Furry Adventure)\nYou can choose who you want to be\n\n"
    )
    ##main menu
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit")

    choice = input("> ")
    if choice == "1":
        startgame()
    elif choice == "2":
        loadgame()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid input")
        time.sleep(2)
        mainmenu()


def startgame():
    while True:
        printn("What should i call you?\n")
        name = input("> ")
        if name == "":
            print("Invalid input")
        else:
            printn(f"do you want {name} as your name")
            confirm = input("> ")
            if confirm == "yes":
                myp.name = name
                break
            else:
                continue
    printn(f"Hey {myp.name}!\nNow you can choose your spieces\n1. Bear\n2.Wolf\n3.Fox")
    while True:
        choice = input("> ")
        if choice == "1":
            myp.species = "Bear"
            # weight in lbs
            myp.weight = 260
            # height in feet
            myp.height = 6.0
            break
        elif choice == "2":
            myp.species = "Wolf"
            myp.weight = 200
            myp.height = 6.0
            break
        elif choice == "3":
            myp.species = "Fox"
            myp.weight = 150
            myp.height = 5.8
            break
        else:
            print("invalid Input")
            continue
    printn(f"Okay {myp.name} you´re a {myp.species} now\n\n")
    ##print Stats
    kg = lbstokg(myp.weight)
    meter = feettometer(myp.height)
    print(
        f"Name:{myp.name}\nSpecies:{myp.species}\nWeight:{myp.weight} lbs/{kg} Kg\nHeight:{myp.height}'/ {meter}M"
    )


if __name__ == "__main__":
    mainmenu()
