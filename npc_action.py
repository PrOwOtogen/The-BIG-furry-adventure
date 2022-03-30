

import time
from rich import print
from rich.console import Console
from ent import *
import os

myp = Player()


def smoothwrite(text, speed):
    for cahar in text:
        print(cahar, end="", flush=True)
        time.sleep(speed)


def smalltalk(npc):
    os.system("cls")
    if npc == "Alex":
        smoothwrite("""
Alex: so, what do you want to talk about?
""", 0.02)
        print("\n[green](1)Tell me something about yourself.[/green]\n(2)[yellow]what do you think about me?[/yellow]\n(3)[red]I don't know what to say.[/red]")
        print("[green]Your choice: [/green]", end="")
        choice = input("").lower().strip()
        os.system("cls")
        if choice == "1":
            text = """
<name>: Tell me something abot yourself. I´d like to know you better.
Alex: I´m Alex, but i think that you already know that. I love collecting things and trade with them, i also have a thing for a bit bigger guys *he begins blushing*. So, what about you?
<name>: I´m a <role> and like to help people out and to travel around.
Alex: Sounds, so what brings you here?
"""
            text = text.replace("<name>", myp.name)
            text = text.replace("<role>", myp.role)
            smoothwrite(text, 0.02)
