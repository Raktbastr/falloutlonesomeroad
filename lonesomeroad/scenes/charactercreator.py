from textual.containers import Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Static, Input, RadioSet, RadioButton
import os
from lonesomeroad import playerdata
from engine.dialogueintrepreter import read_dialogue

class NGScreen(Screen):
    def compose(self):
        yield Static("Type your name below")
        playerdata.NAME = yield Input(placeholder="name")
        pts_left = 0
        with Horizontal():
            with RadioSet(id='STR'):
                yield Static("Strength")
                yield RadioButton('10', disabled=(pts_left < (10-playerdata.STRENGTH) or playerdata.STRENGTH == 10))
                yield RadioButton('9', disabled=(pts_left < (9-playerdata.STRENGTH) or playerdata.STRENGTH == 9))
                yield RadioButton('8', disabled=(pts_left < (8-playerdata.STRENGTH) or playerdata.STRENGTH == 8))
                yield RadioButton('7', disabled=(pts_left < (7-playerdata.STRENGTH) or playerdata.STRENGTH == 7))
                yield RadioButton('6', disabled=(pts_left < (6-playerdata.STRENGTH) or playerdata.STRENGTH == 6))
                yield RadioButton('5', disabled=(pts_left < (5-playerdata.STRENGTH) or playerdata.STRENGTH == 5))
                yield RadioButton('4', disabled=(pts_left < (4-playerdata.STRENGTH) or playerdata.STRENGTH == 4))
                yield RadioButton('3', disabled=(pts_left < (3-playerdata.STRENGTH) or playerdata.STRENGTH == 3))
                yield RadioButton('2', disabled=(pts_left < (2-playerdata.STRENGTH) or playerdata.STRENGTH == 2))
                yield RadioButton('1', disabled=(pts_left < (1-playerdata.STRENGTH) or playerdata.STRENGTH == 1))

    def on_radio_change(self, event: RadioButton.Changed):
        if RadioSet.id == 'STR':
            playerdata.STRENGTH = int(RadioButton.label)
            os.system(f'touch ~/{playerdata.STRENGTH}.txt')



        for line in read_dialogue('intro.vdiag', 1):
            yield Static(line)
        yield Static()