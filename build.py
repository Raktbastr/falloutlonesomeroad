import os
import subprocess
import sys

APP_NAME = "Fallout_Lonesome_Road"   # safe filename
ENTRY_SCRIPT = "main.py"

DATA_FOLDERS = [
    ("assets", "assets"),
    ("engine", "engine"),
    ("lonesomeroad", "lonesomeroad"),
]

DATA_FILES = [
    ("gameinfo.txt", "."),
]

def run(cmd):
    print(f"[RUN] {cmd}")
    subprocess.check_call(cmd, shell=True)

def create_spec_file():
    from pathlib import Path

    spec_path = Path(f"{APP_NAME}.spec")
    if spec_path.exists():
        return

    # Validate data tuples
    datas_list = []
    for entry in DATA_FOLDERS + DATA_FILES:
        if not isinstance(entry, (list, tuple)) or len(entry) != 2:
            raise ValueError(f"DATA entry must be a 2-element tuple: {entry}")
        datas_list.append((entry[0], entry[1]))

    datas_str = ",\n        ".join(
        [f"('{src}', '{dest}')" for src, dest in datas_list]
    )

    spec_text = f'''
block_cipher = None

a = Analysis(
    ['{ENTRY_SCRIPT}'],
    pathex=[],
    binaries=[],
    datas=[{datas_str}],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='{APP_NAME}',
    debug=False,
    strip=False,
    upx=True,
    console=True
)
'''
    spec_path.write_text(spec_text)
    print("Created spec file:", spec_path)


def install_requirements():
    if os.path.exists("requirements.txt"):
        run(f"{sys.executable} -m pip install -r requirements.txt")

def build_app():
    create_spec_file()
    run(f"{sys.executable} -m PyInstaller {APP_NAME}.spec")

def main():
    install_requirements()
    build_app()

if __name__ == "__main__":
    main()
