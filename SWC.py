import os
from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme("BrownBlue")
layout = [
    [sg.Text("Clean temp files?"), sg.Button("Yes",
    size=(15,1),
    tooltip="Cleans all temporary files inside the 'temp' windows folder ",
    key="button_temp_yes"),


    sg.Button("No",
    size=(10,1),
    key="button_temp_no")],

    [sg.Text("Clean local disk?"), sg.Button("Yes",
    size=(15,1),
    tooltip="Free up some storage in local disk by deleting unnecessary files",
    key="button_disk_yes"),

    sg.Button("No", size=(10,1),
    key="button_disk_no")]
]

# Window
window = sg.Window("SWC - Simple Windows Cleaner", layout, size=(350, 100))

def deleting_tempfiles(folder_path):
    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Files successfuly deleted!")
        except:
            print(f"Erro ao deletar os arquivos {file_path}")


folder_path = "C:\\Windows\\Temp"

def window_2():
    layout = [
        [sg.Text("Files  Succesfully cleaned!")],
        [sg.Button("Ok!", key="ok_cleaned_button")]
    ]
    window = sg.Window("Done!", layout, size=(200, 100), finalize=True)
    return window

while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    elif events == "button_temp_yes":
        deleting_tempfiles(folder_path)
        window2 = window_2()
        while True:
            events2, values2 = window2.read()

            if events2 == "ok_cleaned_button" or events2 == sg.WIN_CLOSED():
                break

        window2.close()

    elif events == "button_temp_no":
        print("botão temp no foi ativado!")
    elif events == "button_disk_yes":
        os.system('cmd /k "cleanmgr"')
    elif events == "button_disk_no":
        print("Botão disk no foi ativado!")

window.close()