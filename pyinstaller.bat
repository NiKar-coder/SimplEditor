@echo off
venv\Scripts\pyinstaller.exe --clean --onefile --noconsole --noconfirm --icon="icon.png" --name="SimplEditor" --add-data="icon.png:*" main.py
