import rich
import time
import sys

from characters.player import *
from engine.printn import *
def mainmenu():
    printn("Welcome to TBFA (The Big Furry Adventure)\nYou can choose who you want to be\n\n")
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


def startgame():
    
    while True:
        printn("What should i call you?\n")
        name = input("> ")
        if name == "":
            print("Invalid input")
        else:
            printn(f'do you want {name} as your name')
            confirm = input("> ")
            if confirm == "yes":
                myp.name = name
                break
            else:
                continue


if __name__ == "__main__":
    mainmenu()