from random import randint


class enemy:
    def __init__(self):
        self.name = "enemy"
        self.hp = 0
        self.maxhp = 0
        self.damage = 0
        self.xp = 0
        self.lvl = 1
        self.gold = 0


class alex:
    def __init__(self):
        self.love = 0
        self.inventory = {}

# player


class Player:
    def __init__(self):
        self.name = "ADMIN"
        self.hp = 60
        self.maxhp = 100
        self.atk = 0
        self.defence = 0
        self.role = "ADMIN"
        self.mana = 0
        self.exp = 0
        self.lvl = 1
        self.rep = 0
        self.lust = 0
        self.diff = "easy"
        self.weight = 150
        self.muscle = 120
        self.gold = 10000
        self.loc = "a1"
        self.inv = {
            "sword": 1,
            "shield": 1,
            "potion": 1,
        }
        self.equiped = {}
        self.quests = {}
        self.playermult = 1
        self.enemymult = 1


globitems = {
    "sword": 10,
    "shield": 8,
    "potion": 7,
    "potion2": 8,
    "potion3": 3,
    "food": 4,
}
