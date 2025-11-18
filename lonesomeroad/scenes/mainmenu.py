from textual.screen import Screen
from textual.widgets import Button, TextArea
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
import os

class MenuScreen(Screen):
    def compose(self) -> ComposeResult:
        from main import DATA_DIR
        yield TextArea('Fallout: Lonesome Road')
        yield Horizontal(
            VerticalScroll(
                Button('New Game'),
                Button('Load Game', id='load', disabled=(len(os.path.join(DATA_DIR, 'saves')) == 0)),
                Button('Quit')
            )
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'load':
            self.app.push_screen('load')
