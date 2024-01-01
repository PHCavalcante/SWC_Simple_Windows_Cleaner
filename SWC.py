import os
from PySimpleGUI import PySimpleGUI as sg
import subprocess

# variables
folder_path = "C:\\Windows\\Temp"
folder_path2 = "C:\\Windows\\Prefetch"

sg.theme("BrownBlue")
layout = [
    [sg.Text("Clean temp files?", pad=(0,8)), sg.Button("Yes",
    size=(15,1),
    tooltip="Cleans all temporary files in your PC",
    key="button_temp_yes",
    pad=((25,0)))],

    [sg.Text("Clean local disk?", pad=(0,8)), sg.Button("Yes",
    size=(15,1),
    tooltip="Free up some storage in local disk by deleting unnecessary files",
    key="button_disk_yes",
    pad=((25, 0)))],
]

window = sg.Window("SWC - Simple Windows Cleaner", layout, icon="images/icon.ico")

# Get username for cleaning the %temp% folder

def getting_username():
   username = os.getlogin()
   return username

folder_path3 = f"C:\\Users\\{getting_username()}\\AppData\Local\\Temp"

# Function that cleans the temp folder
def deleting_tempfiles(folder_path):
    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Files successfuly deleted!")
        except:
            print(f"Error! Some files couldn't be deleted!{file_path}")
            print("Maybe it's being used by some open program")


# Function that cleans the prefetch folder
def deleting_prefetch(folder_path2):
    files = os.listdir(folder_path2)

    for file_name in files:
        file_path = os.path.join(folder_path2, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Files successfuly deleted!")
        except:
            print(f"Error! {file_path}")

# Function that cleans the %temp% folder
def deleting_temp2(folder_path3):
    try:
        files = os.listdir(folder_path3)

        for file_name in files:
            file_path = os.path.join(folder_path3, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print("Files successfuly deleted!")
            except:
                print(f"Error! {file_path}")

    except:
        print('Error! Acess Denied!')

def window_2():
    layout = [
        [sg.Text("Files  Succesfully cleaned!")],
        [sg.Button("Ok!", key="ok_cleaned_button", pad=(60,0))]
    ]
    window = sg.Window("Done!", layout, finalize=True, icon="images/icon.ico")
    return window


while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    elif events == "button_temp_yes":
        deleting_tempfiles(folder_path)
        deleting_temp2(folder_path2)
        deleting_prefetch(folder_path3)
        window2 = window_2()
        while True:
            events2, values2 = window2.read()

            if events2 == "ok_cleaned_button" or events2 == sg.WIN_CLOSED():
                break

        window2.close()

    elif events == "button_disk_yes":
        subprocess.Popen(["cmd", "/c", "cleanmgr"])

window.close()
