from textual.screen import Screen
from textual.widgets import Static
import os
from lonesomeroad.playerdata import *

def loadable_amt():
    x = 0
    from main import DATA_DIR
    for file in os.listdir(os.path.join(DATA_DIR, 'saves')):
        if os.path.isfile(os.path.join(DATA_DIR, 'saves', file)) and file.endswith('.vsave'):
            x = x + 1
    return x

class LoadScreen(Screen):
    def compose(self):
        yield Static("Load Screen")

class SaveScreen(Screen):
    def compose(self):
        yield Static("Save Screen")
        yield Static(PREV_SCREEN)