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

from Classes import *
from Textgen import *
from The_Furry_Adventure import assign_weight_range

def talkNPC(who):
    with open("NPCText.json", "r") as f:
        text = json.load(f)
    #NPC Greeting
    #get random greeting from list
    #get greeting for player weight
    weight_range = assign_weight_range(myp.weight)
    try:
        greeting = random.choice(text["NPC"][who]["greeting"][weight_range])
    except:
        greeting =""
        pass
    talk = random.choice(text["NPC"][who]["talk"][weight_range])
    paneltext = greeting + "\n"+ talk
    ##create panel
    panel = Panel(paneltext, title=who)
    print(panel)

    os.system("pause")