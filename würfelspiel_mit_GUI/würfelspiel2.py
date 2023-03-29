# zeigt einen Button der einen Zufallswürfel anzeigt

import random
import PySimpleGUI as sg

codes = {1:"\u2680",
         2:"\u2681",
         3:"\u2682",
         4:"\u2683",
         5:"\u2684",
         6:"\u2685",
         }

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
        window["w1"].update(text=f"{codes[zahl]}")
window.close()

