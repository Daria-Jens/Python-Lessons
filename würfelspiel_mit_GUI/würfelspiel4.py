# zeigt fünf Buttons mit Zufallswürfeln die sich sperren lassen

import random
import PySimpleGUI as sg

codes = {1:"\u2680",
         2:"\u2681",
         3:"\u2682",
         4:"\u2683",
         5:"\u2684",
         6:"\u2685",
         }

gesperrt = {"w1":False,
            "w2":False,
            "w3":False,
            "w4":False,
            "w5":False,
            }

bgcolor = sg.theme_button_color_background()
color = sg.theme_button_color_text()

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
    if event in gesperrt.keys():
        gesperrt[event] = not gesperrt[event]
        if gesperrt[event]:
            window[event].update(button_color=("grey", bgcolor))
        else:
            window[event].update(button_color=(color, bgcolor))
    if event == "würfeln":
        for w in gesperrt.keys():
            if gesperrt[w]:
                continue
            zahl = random.randint(1,6)
            window[w].update(text=f"{codes[zahl]}")
window.close()

