from textual.screen import Screen
from textual.widgets import Static, Button, TextArea
from textual.containers import Horizontal, VerticalScroll
from lonesomeroad import playerdata



class QuitScreen(Screen):
    def compose(self):
        yield TextArea("Are you sure you want to quit?")
        yield Horizontal(
            VerticalScroll(
                Button('Yes', id='yes'),
                Button('No', id='no'),
            )
        )
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'yes':
            self.app.exit()
        if event.button.id == 'no':
            self.app.push_screen(playerdata.PREV_SCREEN)