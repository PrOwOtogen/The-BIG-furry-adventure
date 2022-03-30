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
        #self.lust = 0
        self.diff = "easy"
        self.weight = 0
        self.muscle = 0
        self.gold = 0
        self.loc = "a1"
        self.inv = {
            "sword": 1,
            "shield": 1,
            "potion": 1,
        }
        self.playermult = 1
        self.enemymult = 1
