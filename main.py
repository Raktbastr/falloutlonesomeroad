from textual.app import App, ComposeResult
from textual.widgets import Header, TextArea
import os
import argparse

GAME_NAME = 'unknown'
ALT_GAME_NAME = 'unknown'
GAME_VERSION = 'unknown'
ENGINE_VERSION = 'unknown'
DATA_DIR = 'unknown'

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--gameinfo", help="Path to gameinfo.txt file")
args = parser.parse_args()
if args.gameinfo is None:
    print('App must be run with -g option')
    exit(10)

if not os.path.exists(args.gameinfo):
    print('gameinfo.txt not found at given path')
    exit(10)

if os.name == 'nt':
    DATA_DIR = os.path.join(os.environ['APPDATA'],ALT_GAME_NAME)
elif os.name == 'posix':
    DATA_DIR = f'~/.local/share/{ALT_GAME_NAME}'

with open(args.gameinfo, 'r') as f:
    for line in f.readlines():
        if line.startswith('#'):
            continue
        if line.startswith('NAME'):
            GAME_NAME = line.split('= ')[1].strip()
            continue
        if line.startswith('GAMEVERSION'):
            GAME_VERSION = line.split('= ')[1].strip()
            continue
        if line.startswith('ENGINEVERSION'):
            ENGINE_VERSION = line.split('= ')[1].strip()
            continue


class InitalChecks(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea("Checking Version")

    def on_mount(self) -> None:
        self.title = f'{GAME_NAME}, {GAME_VERSION}'


if __name__ == '__main__':
    InitalChecks().run()