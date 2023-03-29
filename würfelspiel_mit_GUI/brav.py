import PySimpleGUI as sg
sg.PopupOK("Guten Tag")
name = sg.popup_get_text("Wie heißt Du?")
brav = sg.PopupYesNo(f"Warst Du brav, {name} ?")
if brav == "Yes":
    sg.PopupOK("Sehr brav!")
else:
    sg.PopupOK("Schlimmes Kind!")