import io
import os
import sys
from lonesomeroad import playerdata

def resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('./assets/dialogue'), relative_path)

def read_dialogue(file, convo):
    actor = ''
    x = []
    y = []
    startnum = 0
    endnum = 0
    with open (resource_path(file), 'r') as f:
        for idx, line in enumerate(f):
            if line.startswith('actor = '):
                actor = line.strip('actor = ')
            elif line.startswith(f'[START {convo}]'):
                startnum = idx
            elif line.startswith(f'[END {convo}]'):
                endnum = idx
            line.replace('{NAME}', playerdata.NAME)
            x.append(line)
        for idx, line in enumerate(x):
            if startnum < idx < endnum:
                if actor.strip() == 'ignore':
                    y.append(line)
                else:
                    y.append(f'{actor.strip()}: {line}')
        return y





                
                