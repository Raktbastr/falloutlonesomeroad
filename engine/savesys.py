from textual.screen import Screen
from textual.widgets import Static

class LoadScreen(Screen):
    def compose(self):
        yield Static("Load Screen")