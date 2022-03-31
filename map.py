from rich import print
from rich.console import Console

MAP = {
    "a1": {
        "name": "Bedroom",
        "desc": "This is your Bedroom,",
        "isexamined": False,
        "items": {"food": 1,
                  "book": 1,
                  "key": 2},
        "enemy": "none",
        "NPC": "none",
        "isfought": False,
        "UP": "a1",
        "DOWN": "a1",
        "LEFT": "a1",
        "RIGHT": "a2"
    },
    "a2": {
        "name": "hallway",
        "desc": "a Hallway, nothing special",
        "isexamined": False,
        "examine": "theres an Enemy",
        "items": {},
        "enemy": ["bandit", "orc"],
        "NPC": "none",
        "isfought": False,
        "UP": "a2",
        "DOWN": "b2",
        "LEFT": "a1",
        "RIGHT": "a3"
    },
    "a3": {
        "name": "Living Room",
        "desc": "This is the Living Room of the Hotel",
        "isexamined": False,
        "examine": "You can see an muscular Otter",
        "items": {},
        "enemy": "NPC",
        "NPC": "alex_the_merchant",
        "isfought": False,
        "UP": "a3",
        "DOWN": "a3",
        "LEFT": "a2",
        "RIGHT": "a4"
    },
    "a4": {
        "name": "Kitchen",
        "desc": "This is the Kitchen of the Hotel",
        "isexamined": False,
        "examine": "You can see a dirty Kitchen",
        "items": {},
        "enemy": "NPC",
        "NPC": "Jake_the_cook",
        "isfought": False,
        "UP": "a4",
        "DOWN": "a4",
        "LEFT": "a3",
        "RIGHT": "a5"
    },

}
