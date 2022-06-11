import json
import random
from Python.ent import *

myp = Player()

with open("jsons/actions.json", "r") as f:
    rands = json.load(f)


def check_randomactions():
    # 1 - weight
    # 2 - lust
    # 7 - loc
    # 9 - loc + weight
    # 13 - loc + lust
    # weight = magenta1
    # lust = yellow2
    # loc = green

    ret = "[bright_magenta]#" * 50 + "\n"
    typ = random.randint(1, 20)
    typ2 = random.randint(1, 3)
    # print(rands["actions"]['a1']['none']['text']["w<130"])
    if typ == 1:
        # weight
        if typ2 == 1:
            # infos
            if myp.weight < 130:
                ret = random.choice(
                    (rands["actions"]['weight']["infos"]["w<130"]))
            elif myp.weight > 130 and myp.weight < 200:
                ret = random.choice(
                    (rands["actions"]['weight']["infos"]["w>130-200"]))
            elif myp.weight > 200:
                ret = random.choice(
                    (rands["actions"]['weight']["infos"]["w>200"]))
        elif typ2 == 2:
            # actions
            if myp.weight < 130:
                ret = random.choice(
                    (rands["actions"]['weight']["remarks"]["w<130"]))
            elif myp.weight > 130 and myp.weight < 200:
                ret = random.choice(
                    (rands["actions"]['weight']["remarks"]["w>130-200"]))
            elif myp.weight > 200:
                ret = random.choice(
                    (rands["actions"]['weight']["remarks"]["w>200"]))
        elif typ2 == 3:
            # idle
            if myp.weight < 130:
                ret = random.choice(
                    (rands["actions"]['weight']["idle"]["w<130"]))
            elif myp.weight > 130 and myp.weight < 200:
                ret = random.choice(
                    (rands["actions"]['weight']["idle"]["w>130-200"]))
            elif myp.weight > 200:
                ret = random.choice(
                    (rands["actions"]['weight']["idle"]["w>200"]))

    elif typ == 2:
        # lust
        if typ2 == 1:
            if myp.lust < 30:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l<30"]))
            elif myp.lust > 30 and myp.lust < 60:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l>30"]))
            elif myp.lust > 60 and myp.lust < 90:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l>60"]))
            elif myp.lust > 90:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l>90"]))
        elif typ2 == 2:
            if myp.lust < 30:
                ret = random.choice(
                    (rands["actions"]['lust']["remarks"]["l<30"]))
            elif myp.lust > 30 and myp.lust < 60:
                ret = random.choice(
                    (rands["actions"]['lust']["remarks"]["l>30"]))
            elif myp.lust > 60 and myp.lust < 90:
                ret = random.choice(
                    (rands["actions"]['lust']["remarks"]["l>60"]))
            elif myp.lust > 90:
                ret = random.choice(
                    (rands["actions"]['lust']["remarks"]["l>90"]))
        elif typ2 == 3:
            if myp.lust < 30:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l<30"]))
            elif myp.lust > 30 and myp.lust < 60:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l>30"]))
            elif myp.lust > 60 and myp.lust < 90:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l>60"]))
            elif myp.lust > 90:
                ret = random.choice(
                    (rands["actions"]['lust']["infos"]["l>90"]))

    elif typ == 7:
        # loc
        if rands[myp.loc] == None:
            return
        else:
            ret = random.choice(rands[myp.loc]["idle"]["text"])
    elif typ == 9:
        if myp.weight < 130:
            ret = random.choice(
                (rands["actions"]['weight']['idle']["w<130"]))
        elif myp.weight > 130 and myp.weight < 200:
            ret = random.choice(
                (rands["actions"]['weight']['idle']["w>130-200"]))
        elif myp.weight > 200:
            ret = random.choice((rands["actions"]['weight']['idle']["w>200"]))
        ret += random.choice(rands[myp.loc]["idle"]["text"])

    elif myp.hp < 50:
        ret = random.choice(rands["actions"]['health']["infos"]["h<50"])
    return ret
