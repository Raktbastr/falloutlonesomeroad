import os
import pathlib
import sys
from textual.app import App


GAME_NAME = 'unknown'
ALT_GAME_NAME = 'unknown'
VERSION = 'unknown'
DATA_DIR = 'unknown'
HOME = pathlib.Path.home()

def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
GAMEINFO = resource_path('gameinfo.txt')

with open(GAMEINFO, 'r') as f:
    for line in f.readlines():
        if line.startswith('#'):
            continue
        if line.startswith('NAME'):
            GAME_NAME = line.split('= ')[1].strip()
            continue
        if line.startswith('ALTNAME'):
            ALT_GAME_NAME = line.split('= ')[1].strip()
            continue
        if line.startswith('VERSION'):
            VERSION = line.split('= ')[1].strip()
            continue

if os.name == 'nt':
    DATA_DIR = os.path.join(os.environ['APPDATA'],ALT_GAME_NAME)
elif sys.platform == 'darwin':
    DATA_DIR = os.path.join(HOME, 'Library', 'Application Support', ALT_GAME_NAME)
elif os.name == 'posix':
    DATA_DIR = f'~/.local/share/{ALT_GAME_NAME}'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    os.makedirs(os.path.join(DATA_DIR, 'saves'))

class Main(App):
    from engine import savesys
    from lonesomeroad.scenes import mainmenu
    SCREENS = {
        "main": mainmenu.MenuScreen,
        "load": savesys.LoadScreen
    }
    def compose(self):
        return []
    async def on_mount(self):
        await self.app.push_screen('main')

if __name__ == '__main__':
    Main().run()