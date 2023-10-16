import json
import random
import Classes
from Classes import *

def getjson():
    with open("texts/Text.json", "r") as f:
        data = json.load(f)
        return data

def gendescription(what,length):
    data = {}
    if data == {}:
        data = getjson()
    
    if what == "Belly":
        if length == "short":
            ##myp weight switch
            if myp.weight < 100:
                return data["Belly Sizes"]["<100"]["Description"]
            elif myp.weight < 149 and myp.weight >= 100:
                return data["Belly Sizes"]["100-149"]["Description"]
            elif myp.weight < 199 and myp.weight >= 150:
                return data["Belly Sizes"]["150-199"]["Description"]
            elif myp.weight < 249 and myp.weight >= 200:
                return data["Belly Sizes"]["200-249"]["Description"]
            elif myp.weight < 299 and myp.weight >= 250:
                return data ["Belly Sizes"]["250-299"]["Description"]
            elif myp.weight < 349 and myp.weight >= 300:
                return data["Belly Sizes"]["300-349"]["Description"]
            elif myp.weight < 399 and myp.weight >= 350:
                return data["Belly Sizes"]["350-399"]["Description"]
            elif myp.weight < 449 and myp.weight >=400:
                return data["Belly Sizes"]["400-449"]["Description"]
            elif myp.weight < 499 and myp.weight >= 450:
                return data["Belly Sizes"]["450-499"]["Description"]
            elif myp.weight < 599 and myp.weight >= 500:
                return data["Belly Sizes"]["500-599"]["Description"]
            elif myp.weight < 699 and myp.weight >= 600:
                return data["Belly Sizes"]["600-699"]["Description"]
            elif myp.weight < 799 and myp.weight >= 700:
                return data["Belly Sizes"]["700-799"]["Description"]
            elif myp.weight < 899 and myp.weight >= 800:
                return data["Belly Sizes"]["800-899"]["Description"]
            elif myp.weight < 999 and myp.weight >= 900:
                return data["Belly Sizes"]["900-999"]["Description"]
            elif myp.weight < 1099 and myp.weight >= 1000:
                return data["Belly Sizes"]["1000-1099"]["Description"]
            elif myp.weight >= 1200:
                return data["Belly Sizes"][">1200"]["Description"]
        elif length == "long":
            if myp.weight < 100:
                return data["Belly Sizes"]["<100"]["jiggling"]
            elif myp.weight <= 149 and myp.weight >= 100:
                return data["Belly Sizes"]["100-149"]["jiggling"]
            elif myp.weight <= 199 and myp.weight >= 150:
                return data["Belly Sizes"]["150-199"]["jiggling"]
            elif myp.weight <= 249 and myp.weight >= 200:
                return data["Belly Sizes"]["200-249"]["jiggling"]
            elif myp.weight <= 299 and myp.weight >= 250:
                return data ["Belly Sizes"]["250-299"]["jiggling"]
            elif myp.weight <= 349 and myp.weight >= 300:
                return data["Belly Sizes"]["300-349"]["jiggling"]
            elif myp.weight <= 399 and myp.weight >= 350:
                return data["Belly Sizes"]["350-399"]["jiggling"]
            elif myp.weight <= 449 and myp.weight >= 400:
                return data["Belly Sizes"]["400-449"]["jiggling"]
            elif myp.weight <= 499 and myp.weight >= 450:
                return data["Belly Sizes"]["450-499"]["jiggling"]
            elif myp.weight <= 599 and myp.weight >= 500:
                return data["Belly Sizes"]["500-599"]["jiggling"]
            elif myp.weight <= 699 and myp.weight >= 600:
                return data["Belly Sizes"]["600-699"]["jiggling"]
            elif myp.weight <= 799 and myp.weight >= 700:
                return data["Belly Sizes"]["700-799"]["jiggling"]
            elif myp.weight <= 899 and myp.weight >= 800:
                return data["Belly Sizes"]["800-899"]["jiggling"]
            elif myp.weight <= 999 and myp.weight >= 900:
                return data["Belly Sizes"]["900-999"]["jiggling"]
            elif myp.weight <= 1099 and myp.weight >= 1000:
                return data["Belly Sizes"]["1000-1099"]["jiggling"]
            elif myp.weight >= 1200:
                return data["Belly Sizes"][">1200"]["jiggling"]
                
        return "NO SHORT"
    elif what == "legs":
        if length == "short":
            if myp.weight < 100:
                return data["Legs Size"]["<100"]["sDescription"]
            elif myp.weight < 200 and myp.weight > 101:
                return data["Legs Size"]["100-200"]["sDescription"]
            elif myp.weight < 300 and myp.weight > 201:
                return data["Legs Size"]["200-300"]["sDescription"]
            elif myp.weight < 400 and myp.weight > 301:
                return data["Legs Size"]["300-400"]["sDescription"]
            elif myp.weight < 500 and myp.weight > 401:
                return data["Legs Size"]["400-500"]["sDescription"]
            elif myp.weight < 600 and myp.weight > 501:
                return data["Legs Size"]["500-600"]["sDescription"]
            elif myp.weight < 700 and myp.weight > 601:
                return data["Legs Size"]["600-700"]["sDescription"]
            elif myp.weight < 800 and myp.weight > 701:
                return data["Legs Size"]["700-800"]["sDescription"]
            elif myp.weight < 900 and myp.weight > 801:
                return data["Legs Size"]["800-900"]["sDescription"]
            elif myp.weight < 1000 and myp.weight > 901:
                return data["Legs Size"]["900-1000"]["sDescription"]
            elif myp.weight < 1100 and myp.weight > 1001:#
                return data["Legs Size"]["1000-1100"]["sDescription"]
            elif myp.weight > 1200:
                return data["Legs Size"][">1200"]["sDescription"]
        elif length == "long":
            if myp.weight < 100:
                return data["Legs Size"]["<100"]["lDescription"]
            elif myp.weight < 200 and myp.weight > 101:
                return data["Legs Size"]["100-200"]["lDescription"]
            elif myp.weight < 300 and myp.weight > 201:
                return data["Legs Size"]["200-300"]["lDescription"]
            elif myp.weight < 400 and myp.weight > 301:
                return data["Legs Size"]["300-400"]["lDescription"]
            elif myp.weight < 500 and myp.weight > 401:
                return data["Legs Size"]["400-500"]["lDescription"]
            elif myp.weight < 600 and myp.weight > 501:
                return data["Legs Size"]["500-600"]["lDescription"]
            elif myp.weight < 700 and myp.weight > 601:
                return data["Legs Size"]["600-700"]["lDescription"]
            elif myp.weight < 800 and myp.weight > 701:
                return data["Legs Size"]["700-800"]["lDescription"]
            elif myp.weight < 900 and myp.weight > 801:
                return data["Legs Size"]["800-900"]["lDescription"]
            elif myp.weight < 1000 and myp.weight > 901:
                return data["Legs Size"]["900-1000"]["lDescription"]
            elif myp.weight < 1100 and myp.weight > 1001:
                return data["Legs Size"]["1000-1100"]["lDescription"]
            elif myp.weight > 1200:
                return data["Legs Size"][">1200"]["lDescription"]
    elif what == "arm":
        if length == "short":
            if myp.weight > 100:
                return data["Arm Size"]["<100"]["sDescription"]
            elif myp.weight <= 200 and myp.weight > 101:
                return data["Arm Size"]["200"]["sDescription"]
            elif myp.weight <= 300 and myp.weight > 201:
                return data["Arm Size"]["300"]["sDescription"]
            elif myp.weight <= 400 and myp.weight > 301:
                return data["Arm Size"]["400"]["sDescription"]
            elif myp.weight <= 500 and myp.weight > 401:
                return data["Arm Size"]["500"]["sDescription"]
            elif myp.weight <= 600 and myp.weight > 501:
                return data["Arm Size"]["600"]["sDescription"]
            elif myp.weight <= 700 and myp.weight > 601:
                return data["Arm Size"]["700"]["sDescription"]
            elif myp.weight <= 800 and myp.weight > 701:
                return data["Arm Size"]["800"]["sDescription"]
            elif myp.weight <= 900 and myp.weight > 801:
                return data["Arm Size"]["900"]["sDescription"]
            elif myp.weight <= 1000 and myp.weight > 901:
                return data["Arm Size"]["1000"]["sDescription"]
            elif myp.weight <= 1100 and myp.weight > 1001:
                return data["Arm Size"]["1100"]["sDescription"]
            elif myp.weight >= 1200:
                return data["Arm Size"]["1200"]["sDescription"]
        elif length == "long":
            if myp.weight < 100:
                return data["Arm Size"]["<100"]["lDescription"]
            elif myp.weight < 200 and myp.weight > 101:
                return data["Arm Size"]["200"]["lDescription"]
            elif myp.weight < 300 and myp.weight > 201:
                return data["Arm Size"]["300"]["lDescription"]
            elif myp.weight < 400 and myp.weight > 301:
                return data["Arm Size"]["400"]["lDescription"]
            elif myp.weight < 500 and myp.weight > 401:
                return data["Arm Size"]["500"]["lDescription"]
            elif myp.weight < 600 and myp.weight > 501:
                return data["Arm Size"]["600"]["lDescription"]
            elif myp.weight < 700 and myp.weight > 601:
                return data["Arm Size"]["700"]["lDescription"]
            elif myp.weight < 800 and myp.weight > 701:
                return data["Arm Size"]["800"]["lDescription"]
            elif myp.weight < 900 and myp.weight > 801:
                return data["Arm Size"]["900"]["lDescription"]
            elif myp.weight < 1000 and myp.weight > 901:
                return data["Arm Size"]["1000"]["lDescription"]
            elif myp.weight < 1100 and myp.weight > 1001:
                return data["Arm Size"]["1100"]["lDescription"]
            elif myp.weight > 1200:
                return data["Arm Size"]["1200"]["lDescription"]
        
    return "NO WHAT"
def main():
    myp.weight = 250
    data = getjson()
    print(gendescription("Belly", "short"))
    print(gendescription("Belly", "long"))
    print(gendescription("legs", "short"))
    print(gendescription("legs", "long"))
    print(gendescription("arm", "short"))
    print(gendescription("arm", "long"))



main()
