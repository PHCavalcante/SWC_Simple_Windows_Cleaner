import os
from PySimpleGUI import PySimpleGUI as sg
import subprocess
import webbrowser
import requests

# variables
folder_path = "C:\\Windows\\Temp"
folder_path2 = "C:\\Windows\\Prefetch"
#recycle_bin = "C:\\$Recycle.Bin" #Upcoming features
version = "1.1.1"

# Functions

def getting_username():
   username = os.getlogin()
   return username

folder_path3 = f"C:\\Users\\{getting_username()}\\AppData\Local\\Temp"

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

''' #upcoming features
def cleaning_recycle(recycle_bin):
    files = os.listdir(recycle_bin)
    for file_name in files:
        file_path = os.path.join(recycle_bin, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("recycle bin deleted!")
        except:
            print(f"error! {file_path}")
'''
def window_2():
    layout = [
        [sg.Text("Files  Succesfully cleaned!")],
        [sg.Button("Ok!", key="ok_cleaned_button", pad=(60,0))]
    ]
    window = sg.Window("Done!", layout, finalize=True, icon="images/icon.ico")
    return window


def window_update():
    layout = [
        [sg.Text(f"A new version ({latest_version}) is available. Do you want to update?")],
        [sg.Button("Yes", key="Yes_update")], [sg.Button("No", key="No_update")]
    ]
    window = sg.Window("Update", layout, icon="images/icon.ico")
    return window
    
def checking_updates(version):
    response = requests.get("https://github.com/PHCavalcante/SWC_Simple_Windows_Cleaner/releases/latest")
    try:
        response.raise_for_status()
        latest_version = response.json()["tag_name"]

        if latest_version > version:
            return latest_version
        else:
            return None
    except:
        sg.popup_error("Failed to check updates")
        return None

def reading_settings():
    global element, config
    reader = open("settings.ini", "r")
    lines = reader.readlines()
    for line in lines:
        config = line.split(";")

    #print(config)
    element = config[0]
    #print(element)
    return element

def changing_settings():
    global config
    writer = open("settings.ini", "r")
    lines = writer.readlines()
    for line in lines:
        config = line.split(";")

    writer = open("settings.ini", "w")
    for line in lines:
        if line.startswith("["):
            writer.write("\n")
            continue

    writer.write(f"{events}")


sg.theme(reading_settings())

themes = ["BlueMono", "BrownBlue", "DarkBlue12", "DarkBlue14", "DarkGrey13", "Darkteal12"]
menu_def = [['Settings', ['Themes', [themes], 'Check for Updates']], ['Tools', ['Quick Clean']], ['About',
            ['Github', 'Website']], ['Help', ['FAQ']]]
layout = [
    [sg.Menu(menu_def, key='theme')],
    [sg.Text("Clean Temp Files?", justification="c"), sg.Button("Yes",
    size=(20),
    tooltip="Cleans all temporary files in your PC",
    key="button_temp_yes")],

    [sg.Text("Clean Local Disk?", justification="c"), sg.Button("Yes",
    size=(20),
    tooltip="Free up some storage in local disk by deleting unnecessary files",
    key="button_disk_yes")],
]

window = sg.Window("SWC - Simple Windows Cleaner", layout, icon="images/icon.ico")


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

    elif events in themes:
        try:
            changing_settings()
            sg.popup("Theme successfuly changed!, please restart the program", title="Success!", icon="images/icon.ico")
        except Exception as e:
            sg.popup(f"Error {e} while changing theme!")

    elif events == 'Github':
        try:
            webbrowser.open('https://github.com/PHCavalcante/SWC_Simple_Windows_Cleaner')
        except:
            sg.popup('Error! failed opening browser')

    elif events == 'Website':
        try:
            webbrowser.open('https://phcavalcante.github.io/SWC-Site/')
        except:
            sg.popup_error('Error! failed opening browser')
    elif events == 'FAQ':
        webbrowser.open('https://phcavalcante.github.io/SWC-Site/pages/faq.html')
    elif events == 'Quick Clean':
        deleting_tempfiles(folder_path)
        deleting_temp2(folder_path2)
        deleting_prefetch(folder_path3)
        os.popen('cleanmgr.exe /sagerun:1')

    elif events == 'Check for Updates':
        latest_version = checking_updates(version)

        if latest_version:
            window_update()
            if events == "yes_update":
                webbrowser.open("https://github.com/PHCavalcante/SWC_Simple_Windows_Cleaner/raw/main/SWC.exe")
                sg.popup("New version downloaded! opening the new version...")
                try:
                    os.startfile(f"C:\\Users\\{getting_username()}\\Downloads\\SWC.py")
                    window.close()
                except:
                    sg.popup("Failed executing new version! make sure to download the new version to your 'downloads "
                             "folder'")
            else:
                sg.popup("No updates occurred.")
        else:
            sg.popup("You are using the latest version.", title="Up To Date", icon="images/icon.ico")

window.close()
