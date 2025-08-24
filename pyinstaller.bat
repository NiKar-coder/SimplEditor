@echo off
venv\Scripts\pyinstaller.exe --clean --distpath "." --onefile --noconsole --noconfirm --icon "data/icons/icon.png" --name "SimplEditor" --add-data "data/icons/icon.png:." main.py
