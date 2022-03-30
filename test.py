
import json
import random


with open('jsons/actions.json', 'r') as f:
    data = json.load(f)

print(random.choice(data["actions"]['a1']['none']['text']["w<130"]))
