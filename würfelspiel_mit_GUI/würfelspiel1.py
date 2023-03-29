# zeigt einen Button der eine Zufallszahl anzeigt

import random
import PySimpleGUI as sg

layout = [
    [sg.Button("?", key="w1", font=("System",64))],
    [sg.Button("Cancel")],
]

window = sg.Window("kleines Programm", layout)

while True:
    event, values = window.read()
    if event in ("Cancel", sg.WIN_CLOSED):
        break
    if event == "w1":
        zahl = random.randint(1,6)
        window["w1"].update(text=f"{zahl}")
window.close()