import json
import os
import sys

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

W_FISTS = find('Fists')
def fists_calc():
    from lonesomeroad.playerdata import STRENGTH
    # Ignore fists when calculating bash damage later!
    if W_FISTS['dmg'] <= 0:
        W_FISTS['dmg'] = 2
    if STRENGTH <= 4:
        W_FISTS['desc'] = W_FISTS['desc'] + "a last resort"
    elif STRENGTH <= 8:
        W_FISTS['desc'] = W_FISTS['desc'] + "use cautiously"
    else:
        W_FISTS['desc'] = W_FISTS['desc'] + "a formidable weapon."

W_COMBATKNIFE = find('Combat Knife')
W_RIPPER = find('Ripper')
W_CHAINSAW = find('Chainsaw')
W_BASEBALLBAT = find('Baseball Bat')
W_POWERFIST = find('Power Fist')
W_SUPERSLEDGE = find('Super Sledge')
W_10MMPISTOL = find('10mm Pistol')
W_HUNTINGRIFLE = find('Hunting Rifle')