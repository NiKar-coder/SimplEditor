@echo off
venv\Scripts\pyinstaller.exe --clean --onefile --noconsole --noconfirm --icon "data\icons\icon.png" --name "SimplEditor" main.py
