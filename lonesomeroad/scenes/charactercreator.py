from textual.screen import Screen
from textual.widgets import Static

from engine.dialogueintrepreter import read_dialogue
from lonesomeroad import playerdata
from engine import dialogueintrepreter

class NGScreen(Screen):
    def compose(self):
        for line in read_dialogue('intro.vdiag', 1):
            yield Static(line)
        yield Static()