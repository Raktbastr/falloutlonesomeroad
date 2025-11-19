from textual.screen import Screen
from textual.widgets import Button, TextArea
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from engine.savesys import loadable_amt
from lonesomeroad import playerdata

class MenuScreen(Screen):
    def compose(self) -> ComposeResult:
        yield TextArea('Fallout: Lonesome Road')
        yield Horizontal(
            VerticalScroll(
                Button('New Game', id='new'),
                Button('Load Game', id='load', disabled=(loadable_amt() == 0)),
                Button('Quit', id='quit')
            )
        )
    def on_button_pressed(self, event: Button.Pressed):
        playerdata.PREV_SCREEN = 'main'
        if event.button.id == 'load':
            self.app.push_screen('load')
        if event.button.id == 'new':
            self.app.push_screen('create_character')
        if event.button.id == 'quit':
            self.app.push_screen('quit')
