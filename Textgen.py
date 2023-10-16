import random
import json
from tkinter import TOP
from Classes import *
from The_Furry_Adventure import printn
data = {}

def getjson():
    with open ("texts/Text.json", "r") as f:
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
    elif what == "Clean":
        if length == "short":
            #if myp.clean is between 0 nad 20
            if myp.clean <= 20:
                return data["Clean"]["0"]["sDescription"]
            elif myp.clean <= 40 and myp.clean > 20:
                return data["Clean"]["20"]["sDescription"]
            elif myp.clean <= 60 and myp.clean > 40:
                return data["Clean"]["40"]["sDescription"]
            elif myp.clean <= 80 and myp.clean > 60:
                return data["Clean"]["60"]["sDescription"]
            elif myp.clean <= 95 and myp.clean > 80:
                return data["Clean"]["80"]["sDescription"]
            elif myp.clean <= 100 and myp.clean > 95:
                return data["Clean"]["95"]["sDescription"]
        elif length == "long":
            if myp.clean <= 20:
                return data["Clean"]["0"]["lDescription"]
            elif myp.clean <= 40 and myp.clean > 20:
                return data["Clean"]["20"]["lDescription"]
            elif myp.clean <= 60 and myp.clean > 40:
                return data["Clean"]["40"]["lDescription"]
            elif myp.clean <= 80 and myp.clean > 60:
                return data["Clean"]["60"]["lDescription"]
            elif myp.clean <= 95 and myp.clean > 80:
                return data["Clean"]["80"]["lDescription"]
            elif myp.clean <= 100 and myp.clean > 95:
                return data["Clean"]["95"]["lDescription"]
        elif length == "scent":
            if myp.clean <= 20:
                return data["Clean"]["0"]["Scent"]
            elif myp.clean <= 40 and myp.clean > 20:
                return data["Clean"]["20"]["Scent"]
            elif myp.clean <= 60 and myp.clean > 40:
                return data["Clean"]["40"]["Scent"]
            elif myp.clean <= 80 and myp.clean > 60:
                return data["Clean"]["60"]["Scent"]
            elif myp.clean <= 95 and myp.clean > 80:
                return data["Clean"]["80"]["Scent"]
            elif myp.clean <= 100 and myp.clean > 95:
                return data["Clean"]["95"]["Scent"]


    return "NO WHAT"


##IDLE TEXT
def idletext():
    c = random.randint(1, 10)
    data = getjson()
    #weight <100, 100-149, 150-199,200-249,250-299,300-349,350-399,400-449,450-499,500-599,600-699,700-799,800-899,900-999,1000-1199,1200<
    if myp.weight <= 100:
        ##random choice between 1 and 10    
        r = data["idle"]['<100'][str(c)]
        printn(r,0.5)

    elif myp.weight <= 150 and myp.weight > 100:
        r = data["idle"]["100-149"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 200 and myp.weight > 150:
        r = data["idle"]["150-199"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 250 and myp.weight > 200:
        
        r = data["idle"]["200-249"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 300 and myp.weight > 250:
        r = data["idle"]["250-299"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 350 and myp.weight > 300:
        r = data["idle"]["300-349"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 400 and myp.weight > 350:
        r = data["idle"]["350-399"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 450 and myp.weight > 400:
        r = data["idle"]["400-449"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 500 and myp.weight > 450:
        r = data["idle"]["450-499"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 600 and myp.weight > 500:
        r = data["idle"]["500-599"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 700 and myp.weight > 600:
        r = data["idle"]["600-699"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 800 and myp.weight > 700:
        r = data["idle"]["700-799"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 900 and myp.weight > 800:
        r = data["idle"]["800-899"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 1000 and myp.weight > 900:
        r = data["idle"]["900-999"][str(c)]
        printn(r,0.5)
    elif myp.weight <= 1200 and myp.weight > 1000:
        r = data["idle"]["1000-1199"][str(c)]
        printn(r,0.5)
    elif myp.weight >= 1200:
        r = data["idle"]["1200<"][str(c)]
        printn(r,0.5)
    
def lustinf():
    c = random.randint(1, 10)
    data = getjson()
    if myp.lust == 0:
        r = "you are not horny at all"
        printn(r,0.5)
    elif myp.lust <= 1 and myp.lust > 20:
        r = data["lust"]["0-19"][str(c)]
        printn(r,0.5)
    elif myp.lust <= 20 and myp.lust > 39:
        r = data["lust"]["20-39"][str(c)]
        printn(r,0.5)
    elif myp.lust <= 40 and myp.lust > 59:
        r = data["lust"]["40-59"][str(c)]
        printn(r,0.5)
    elif myp.lust <= 60 and myp.lust > 79:
        r = data["lust"]["60-79"][str(c)]
        printn(r,0.5)
    elif myp.lust <= 80 and myp.lust <= 100:
        r = data["lust"]["80-100"][str(c)]
        printn(r,0.5)
    
def dirtyinf():
    c = random.randint(1, 10)
    data = getjson()
    if myp.filth >= 100 and myp.filth <= 79:
        r = data["filthy"]["100-79"][str(c)]
        printn(r,0.5)
    elif myp.filth >= 78 and myp.filth <= 59:
        r = data["filthy"]["78-59"][str(c)]
        printn(r,0.5)
    elif myp.filth >= 58 and myp.filth <= 39:
        r = data["filthy"]["58-39"][str(c)]
        printn(r,0.5)
    elif myp.filth >= 38 and myp.filth <= 19:
        r = data["filthy"]["38-19"][str(c)]
        printn(r,0.5)
    elif myp.filth >= 18 and myp.filth <= 0:
        r = data["filthy"]["18-0"][str(c)]
        printn(r,0.5)
    


##TODO
      
def getappearence():
    fur_color = ""
    fur_texture = ""
    slegs = gendescription("legs", "short")
    belly_shape = gendescription("Belly", "short")
    belly_movement = gendescription("Belly", "long")
    arms_type = gendescription("arm", "short")
    scent_strength = gendescription("Clean", "short")
    scent_type = gendescription("Clean", "long")
    sweat_smell = gendescription("Clean", "scent")
    time_traveling = myp.lastshower 
    if myp.furcolor == "":
        fur_color = ""
    if myp.furtexture == "":
        fur_texture = ""
    text = f"""
General Info:
{myp.name} is a {myp.species} standing at {myp.height} feet tall on their {slegs} Legs. Their fur is {fur_color} and is {fur_texture}. They have a {belly_shape} belly. {belly_movement}, your arms at a {arms_type} size.\n\n

Scent Info:
{myp.name} has a {scent_strength} and {scent_type} scent, common to their species. They have been traveling for {time_traveling} days without a shower. {sweat_smell}.
    
    """
    return text
         