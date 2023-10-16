##create class player
class Player:
    def __init__(self):
        self.name = ""
        self.health = 150
        self.weight = 360
        self.defense = 100
        self.height = 6.1
        self.filth = 20
        self.clean = 100 - self.filth
        self.speed = 0
        self.attack = 0
        self.lust = 0
        self.species = ""
        self.armor = {}
        self.inventory = {}
        self.location = "start"
        self.status_effects = []
        self.health_issues = {}
        self.sizes = {
            "dick": 0,
            "chest": 0,
            "arms": 0,
            "legs": 0,
            "belly": 0,
            "balls": 0,
        }
        self.addedsizes = {
            "dick": 0,
            "chest": 0,
            "arms": 0,
            "legs": 0,
            "belly": 0,
            "balls": 0,
        }
        self.normalsizes = {
            "dick": 5,
            "chest": 0,
            "arms": 0,
            "legs": 0,
            "belly": 0,
            "balls": 3,
        }
        self.quests = []
        self.gold = 0
        self.xp = 0
        self.level = 1
        self.max_health = 100
        self.max_weight = 360
        self.max_lust = 100
        self.max_xp = 100
        self.height = 0
        self.furcolor = ""
        self.furtexture = ""
        self.lastshower = 0
        self.lastfood = 0
        self.lastsleep = 0
        self.lastpee = 0
        self.lastpoo = 0
        self.lastcum = 0
        self.days = 0
        self.hunger = 0
        self.thirst = 0


myp = Player()


##create class enemy
class Enemy:
    def __init__(self):
        self.level = 0
        self.health = 0
        self.max_health = 0
        self.attack = 0
        self.defense = 0
        self.lust = 0
