from utils.PlayerEnyClass import *


def calcstats():
    if myp.species == "wolf":
        myp.height = 180
        myp.health = 150
        myp.weight = 180
        myp.defense = 4
        myp.speed = 60
        myp.clean = 89
        myp.attack = 6
        myp.lust = 20
        myp.furcolor = "grey"
        myp.max_health = myp.health
    elif myp.species == "lion":
        myp.height = 180
        myp.health = 140
        myp.weight = 200
        myp.defense = 4
        myp.speed = 65
        myp.clean = 90
        myp.attack = 5
        myp.lust = 15
        myp.furcolor = "golden"
        myp.max_health = myp.health
    elif myp.species == "tiger":
        myp.height = 180
        myp.health = 140
        myp.weight = 200
        myp.defense = 4
        myp.speed = 65
        myp.clean = 90
        myp.attack = 5
        myp.lust = 15
        myp.furcolor = "orange"
        myp.max_health = myp.health
    elif myp.species == "bear":
        myp.height = 180
        myp.health = 200
        myp.weight = 250
        myp.defense = 6
        myp.speed = 50
        myp.clean = 80
        myp.attack = 7
        myp.lust = 25
        myp.furcolor = "brown"
        myp.max_health = myp.health
    elif myp.species == "fox":
        myp.height = 180
        myp.health = 100
        myp.weight = 120
        myp.defense = 2
        myp.speed = 80
        myp.clean = 95
        myp.attack = 4
        myp.lust = 50
        myp.furcolor = "red"
        myp.max_health = myp.health
