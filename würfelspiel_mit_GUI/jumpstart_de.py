import PySimpleGUI as sg

sg.theme('Green')   # Farbschema

# Das Layout ist eine Liste mit Listen. 
# Jede innere Liste ist eine GUI-Zeile 
layout = [ 
    [sg.Text('Deine letzte Eingabe war:'),
     sg.Text("...", key="text1", font=("System", 64))],
    [sg.Text('Schreib etwas in Linie 2:'), sg.InputText(key="antwort1", )],
    [sg.Button('Ok', bind_return_key=True),  sg.Button('Cancel')],
]

# Fenstertitel und Layout festlegen:
window = sg.Window('Mein GUI', layout)
# Die Endlosschleife erzeugt 'events' und alle Eingabefelder erzeugen 'values' 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if event == "Ok": 
        usertext = values["antwort1"] # oder values[0]
        window["text1"].update(f"{usertext}")

window.close()