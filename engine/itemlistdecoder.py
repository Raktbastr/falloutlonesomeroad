import json
import os
import sys
from lonesomeroad import playerdata

def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("./lonesomeroad"), relative_path)

WLIST_PATH = resource_path('../assets/weapons.json')
ALIST_PATH = resource_path('../assets/armors.json')
decoder = json.JSONDecoder()

def find(name, list):
    with open(list, 'r') as f:
        item_data = json.load(f)
        for item in item_data:
            if item['name'] == name:
                return item
            continue


W_FISTS = find('Fists', WLIST_PATH)
def fists_calc():
    if W_FISTS['dmg'] <= 0:
        W_FISTS['dmg'] = -2
    if playerdata.STRENGTH <= 4:
        W_FISTS['desc'] = W_FISTS['desc'] + "a last resort"
    elif playerdata.STRENGTH <= 8:
        W_FISTS['desc'] = W_FISTS['desc'] + "use cautiously"
    else:
        W_FISTS['desc'] = W_FISTS['desc'] + "a formidable weapon."

W_COMBATKNIFE = find('Combat Knife', WLIST_PATH)
W_RIPPER = find('Ripper', WLIST_PATH)
W_CHAINSAW = find('Chainsaw', WLIST_PATH)
W_BASEBALLBAT = find('Baseball Bat', WLIST_PATH)
W_POWERFIST = find('Power Fist', WLIST_PATH)
W_SUPERSLEDGE = find('Super Sledge', WLIST_PATH)
W_10MMPISTOL = find('10mm Pistol', WLIST_PATH)
W_HUNTINGRIFLE = find('Hunting Rifle', WLIST_PATH)

