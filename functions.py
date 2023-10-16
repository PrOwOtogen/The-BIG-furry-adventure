import json
from Classes import *
import os
import sys


def getmap():
    with open("map.json", "r") as f:
        map = json.load(f)
    return map


def getitems():
    with open("items.json", "r") as f:
        items = json.load(f)
    return items


def gettypeofitem(item):
    items = getitems()
    for m in items:
        for s in items[m]:
            for i in items[m][s]:
                if i == item:
                    # print("Item: " + i)
                    # print("Type: " + m)
                    # print("Subtype: " + s)
                    # print("typeofitem: " + items[m][s][i]["type"])
                    return items[m][s][i]["type"]


def getiteminfo(item):
    items = getitems()
    for m in items:
        for s in items[m]:
            for i in items[m][s]:
                if i == item:
                    return m, s


def save(map):
    with open(myp.name + ".json", "w") as f:
        player = myp.__dict__  # convert to dict to save

        savetext = {"player": player, "map": map}  # save player  # save map
        json.dump(savetext, f, indent=4)

        print(
            "Game saved!\npath to save file: " + os.getcwd() + "\\" + myp.name + ".json"
        )

        os.system("pause")


def calcstats():
    girth = assign_weight_girth(myp.weight)
    chest = girth[0]
    arms = girth[1]
    legs = girth[2]
    belly = girth[3]
    myp.normalsizes["chest"] = chest
    myp.normalsizes["arms"] = arms
    myp.normalsizes["legs"] = legs
    myp.normalsizes["belly"] = belly

    myp.sizes["chest"] = myp.normalsizes["chest"] + myp.addedsizes["chest"]
    myp.sizes["arms"] = myp.normalsizes["arms"] + myp.addedsizes["arms"]
    myp.sizes["legs"] = myp.normalsizes["legs"] + myp.addedsizes["legs"]
    myp.sizes["belly"] = myp.normalsizes["belly"] + myp.addedsizes["belly"]
    myp.sizes["balls"] = myp.normalsizes["balls"] + myp.addedsizes["balls"]
    myp.sizes["dick"] = myp.normalsizes["dick"] + myp.addedsizes["dick"]


def assign_weight_range(player_weight):
    if player_weight < 100:
        return "<100"
    elif 100 <= player_weight <= 149:
        return "100-149"
    elif 150 <= player_weight <= 199:
        return "150-199"
    elif 200 <= player_weight <= 249:
        return "200-249"
    elif 250 <= player_weight <= 299:
        return "250-299"
    elif 300 <= player_weight <= 349:
        return "300-349"
    elif 350 <= player_weight <= 399:
        return "350-399"
    elif 400 <= player_weight <= 449:
        return "400-449"
    elif 450 <= player_weight <= 499:
        return "450-499"
    elif 500 <= player_weight <= 599:
        return "500-599"
    elif 600 <= player_weight <= 699:
        return "600-699"
    elif 700 <= player_weight <= 799:
        return "700-799"
    elif 800 <= player_weight <= 899:
        return "800-899"
    elif 900 <= player_weight <= 999:
        return "900-999"
    elif 1000 <= player_weight <= 1199:
        return "1000-1199"
    else:
        return "1200<"


def assign_weight_girth(player_weight):
    if player_weight < 100:
        c = round((30 + 32) / 2)
        a = round((10 + 11) / 2)
        l = round((18 + 20) / 2)
        b = round((28 + 30) / 2)
        return c, a, l, b
    elif 100 <= player_weight <= 149:
        c = round((34 + 36) / 2)
        a = round((11 + 13) / 2)
        l = round((20 + 22) / 2)
        b = round((30 + 32) / 2)
        return c, a, l, b
    elif 150 <= player_weight <= 199:
        c = round((38 + 40) / 2)
        a = round((13 + 15) / 2)
        l = round((22 + 24) / 2)
        b = round((32 + 34) / 2)
        return c, a, l, b
    elif 200 <= player_weight <= 249:
        c = round((42 + 44) / 2)
        a = round((15 + 17) / 2)
        l = round((24 + 26) / 2)
        b = round((34 + 36) / 2)
        return c, a, l, b
    elif 250 <= player_weight <= 299:
        c = round((46 + 48) / 2)
        a = round((17 + 19) / 2)
        l = round((26 + 28) / 2)
        b = round((36 + 38) / 2)
        return c, a, l, b
    elif 300 <= player_weight <= 349:
        c = round((50 - 52) / 2)
        a = round((19 + 21) / 2)
        l = round((28 + 30) / 2)
        b = round((46 + 50) / 2)
        return c, a, l, b

    elif 350 <= player_weight <= 399:
        c = round((54 + 56) / 2)
        a = round((21 + 23) / 2)
        l = round((30 + 32) / 2)
        b = round((52 + 54) / 2)
        return c, a, l, b
    elif 400 <= player_weight <= 449:
        c = round((58 + 60) / 2)
        a = round((23 + 25) / 2)
        l = round((32 + 34) / 2)
        b = round((54 + 56) / 2)
        return c, a, l, b
    elif 450 <= player_weight <= 499:
        c = round((62 + 64) / 2)
        a = round((25 + 27) / 2)
        l = round((34 + 36) / 2)
        b = round((56 + 60) / 2)
        return c, a, l, b

    elif 500 <= player_weight <= 599:
        c = round((66 + 68) / 2)
        a = round((27 + 29) / 2)
        l = round((36 + 38) / 2)
        b = round((62 + 64) / 2)
        return c, a, l, b
    elif 600 <= player_weight <= 699:
        c = round((70 + 72) / 2)
        a = round((29 + 31) / 2)
        l = round((38 + 40) / 2)
        b = 69
        return c, a, l, b
    elif 700 <= player_weight <= 799:
        c = round((74 + 76) / 2)
        a = round((31 + 33) / 2)
        l = round((40 + 42) / 2)
        b = 84
        return c, a, l, b
    elif 800 <= player_weight <= 899:
        c = round((78 + 80) / 2)
        a = round((33 + 35) / 2)
        l = round((42 + 44) / 2)
        b = 100
        return c, a, l, b
    elif 900 <= player_weight <= 999:
        c = round((82 + 84) / 2)
        a = round((35 + 37) / 2)
        l = round((44 + 46) / 2)
        b = 105
        return c, a, l, b
    elif 1000 <= player_weight <= 1199:
        c = round((86 + 88) / 2)
        a = round((37 + 39) / 2)
        l = round((46 + 48) / 2)
        b = 110
        return c, a, l, b
    else:
        c = round((90 + 92) / 2)
        a = round((39 + 41) / 2)
        l = round((48 + 50) / 2)
        b = 125
        return c, a, l, b
