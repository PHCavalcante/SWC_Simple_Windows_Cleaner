import os
from PySimpleGUI import PySimpleGUI as sg
import subprocess

# variables
folder_path = "C:\\Windows\\Temp"
folder_path2 = "C:\\Windows\\Prefetch"
command = "sfc /scannow"

sg.theme("BrownBlue")
layout = [
    [sg.Text("Clean temp files?"), sg.Button("Yes",
    size=(15,1),
    tooltip="Cleans all temporary Windows files",
    key="button_temp_yes"),

    sg.Button("No",
    size=(10,1),
    key="button_temp_no")],

    [sg.Text("Clean local disk?"), sg.Button("Yes",
    size=(15,1),
    tooltip="Free up some storage in local disk by deleting unnecessary files",
    key="button_disk_yes"),

    sg.Button("No", size=(10,1),
    key="button_disk_no")],

]
# Upcoming features
'''
[sg.Text("Run integrity check?"), sg.Button("Yes",
size=(15,1),
tooltip="Runs a integrity check in system files and fix if erros are found",
key="button_integrity_yes"),

sg.Button("No", size=(10,1),
key="button_integrity_no")]
'''

window = sg.Window("SWC - Simple Windows Cleaner", layout, size=(370, 80), icon="images/icon.ico")

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
            print(f"Error! {file_path}")


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
    files = os.listdir(folder_path3)

    for file_name in files:
        file_path = os.path.join(folder_path3, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Files successfuly deleted!")
        except:
            print(f"Error! {file_path}")

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
        deleting_temp2(folder_path2)
        deleting_prefetch(folder_path3)
        window2 = window_2()
        while True:
            events2, values2 = window2.read()

            if events2 == "ok_cleaned_button" or events2 == sg.WIN_CLOSED():
                break

        window2.close()

    elif events == "button_temp_no":
        '''
        NOTE: this is just for testing purposes. and for not leaving the loop without lines of code.
        also because I have no idea of what to put here.
        '''

        print("temp no button activated!")
    elif events == "button_disk_yes":
        subprocess.Popen(["cmd", "/c", "cleanmgr"])

    elif events == "button_disk_no":
        '''
        NOTE: this is just for testing purposes. and for not leaving the loop without lines of code.
        also because I have no idea of what to put here.
        '''

        print("disk no button activated!")

    # Upcoming features
    '''
    elif events == "button_integrity_yes":
        try:
            
            subprocess.Popen(['runas', '/user:Administrator', 'sfc /scannow'])
        except subprocess.CalledProcessError as e:
            print("Error! failed to run.")
            print(f"{e}")
    '''

window.close()
