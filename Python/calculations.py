
import time
from rich import print
from rich.console import Console
import random
from Python.ent import *

myp = Player()
eny = enemy()


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
    r = random.randint(1, 5)
    while eny.damage * r - myp.defence <= 0:
        eny.damage += 0.5
        print(eny.damage)

    dmg = eny.damage + ((eny.lvl*myp.enemymult) / eny.damage * r - myp.defence)
    if dmg < 0:
        eny.damage += 1
        cal_enydmg()
    return dmg
