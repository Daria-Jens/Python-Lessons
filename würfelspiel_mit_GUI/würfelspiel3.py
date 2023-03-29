# zeigt fünf Buttons mit Zufallswürfeln

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
    [sg.Button("?", key="w1", font=("System",64)),
     sg.Button("?", key="w2", font=("System",64)),
     sg.Button("?", key="w3", font=("System",64)),
     sg.Button("?", key="w4", font=("System",64)),
     sg.Button("?", key="w5", font=("System",64)),     
    ],
    [sg.Button("Cancel"), sg.Button("würfeln")],
]

window = sg.Window("kleines Programm", layout)

while True:
    event, values = window.read()
    if event in ("Cancel", sg.WIN_CLOSED):
        break
    if event in ("w1","w2","w3","w4","w5"):
        zahl = random.randint(1,6)
        window[event].update(text=f"{codes[zahl]}")
    if event == "würfeln":
        for w in ("w1","w2","w3","w4","w5"):
            zahl = random.randint(1,6)
            window[w].update(text=f"{codes[zahl]}")
window.close()

