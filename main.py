import customtkinter as ctk
import os
import subprocess
import webbrowser
import requests
from PIL import Image
import json
from packaging import version

settings_path = "settings.json"

with open(settings_path, "r") as json_file:
    config = json.load(json_file)

window = ctk.CTk()
window.title("SWC")
window.geometry("900x500")
ctk.set_appearance_mode(config["GUI"]["aparence_mode"])
window.resizable(width=False, height=False)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
window.iconbitmap("images/icon.ico")


def getting_username():
   username = os.getlogin()
   return username


def popup(title, text1, text2 ,text_button):
    p = ctk.CTk()
    p.title(title)
    p.geometry("300x120")
    p.resizable(False, False)
    p.iconbitmap("images/icon.ico")
    label = ctk.CTkLabel(p, text=text1).pack(pady=10)
    label2 = ctk.CTkLabel(p, text=text2).pack(pady=10)
    button = ctk.CTkButton(p, text=text_button).pack(pady=10)
    p.mainloop()
    p.destroy()

def updating():
    webbrowser.open("")
    pass


def popup_update(title):
    p = ctk.CTkToplevel()
    p.title(title)
    p.geometry("400x90")
    p.resizable(False, False)
    p.after(200, lambda: p.iconbitmap(f"C:\\Users\\{getting_username()}\\Desktop\\SWC_Simple_Windows_Cleaner\\images\\icon.ico"))
    label = ctk.CTkLabel(p, text="There's a update avaliable, do you want to update know?", font=("Segoe UI", 15)).pack(pady=5)
    button1 = ctk.CTkButton(p, text="Yes", corner_radius=15, ).place(x=50, y=50)
    button2 = ctk.CTkButton(p, text="No", corner_radius=15, command=p.destroy).place(x=200, y=50)


def help():
    webbrowser.open("https://phcavalcante.github.io/SWC-Site/pages/faq.html")


def cleaning():
    folder_path = "C:\\Windows\\Temp"
    folder_path2 = "C:\\Windows\\Prefetch"
    folder_path3 = f"C:\\Users\\{getting_username()}\\AppData\Local\\Temp"
    files = os.listdir(folder_path)
    files2 = os.listdir(folder_path2)
    files3 = os.listdir(folder_path3)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Temp Files successfuly deleted!")
        except Exception as error:
            print()
    for file_name in files2:
        file_path = os.path.join(folder_path2, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Prefech files deleted!")
        except Exception as error:
            cause = str(error)
            print(cause)
            if cause.startswith("[WinError 5"):
               print()
    for file_name in files3:
        file_path = os.path.join(folder_path3, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("%Temp% files deleted")
        except Exception as cause:
            print()

    c = ctk.CTkToplevel()
    c.title("Cleaning")
    c.geometry("300x120")
    c.resizable(False, False)
    pg_bar = ctk.CTkProgressBar(c, width=150, height=15, corner_radius=50)
    pg_bar.pack()


def getting_recycle_size():
    recycle_path = "C:\\$Recycle.Bin"
    size = 0
    for file in os.scandir(recycle_path):
        if file.is_file():
            size += os.path.getsize(file.path)
    size = size / (1024 ** 2)
    return f"{size:.2f}" + "MB"

def cleaning_recycle():
    while True:
        if getting_recycle_size().startswith("0.0"):
            break
        else:
            recycle_path = "C:\\$Recycle.Bin"
            files = os.listdir(recycle_path)
            for file_name in files:
                file_path = os.path.join(recycle_path, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print("Temp Files successfuly deleted!")
                except Exception as cause:
                    popup("Could Not Delete Some Files", f"Erro: {cause}", "I dont know what kind of error could happen while trying clean the recycle bin so, I cannot even suggest you a fix.","Ok")


def disk_cleanup():
    subprocess.Popen(["cmd", "/c", "cleanmgr"])
def paths():
    string = f"C:\\Windows\\Temp      C:\\Windows\\Prefetch      C:\\Users\\{getting_username()}\\AppData\Local\\Temp"
    return string
def getting_size():
    folder_path = "C:\\Windows\\Temp"
    folder_path2 = "C:\\Windows\\Prefetch"
    folder_path3 = f"C:\\Users\\{getting_username()}\\AppData\Local\\Temp"
    size = 0
    for file in os.scandir(folder_path):
        if file.is_file():
            size += os.path.getsize(file.path)
    for file in os.scandir(folder_path2):
        if file.is_file():
            size += os.path.getsize(file.path)
    for file in os.scandir(folder_path3):
        if file.is_file():
            size += os.path.getsize(file.path)
    size = size / (1024 ** 2)
    return f"{size:.2f}" + "MB"

def checking_updates():
    repository_url = "https://api.github.com/repos/PHCavalcante/SWC_Simple_Windows_Cleaner/releases/latest"
    try:
        response = requests.get(repository_url)
        response.raise_for_status()
        requesting_version = response.json()["tag_name"]

        latest_version = version.parse(requesting_version)
        current_version = version.parse("v2.0.0")

        if latest_version > current_version:
            popup_update("Update Avaliable")

        else:
            s = ctk.CTkToplevel()
            s.title("Up To Date!")
            s.geometry("250x90")
            s.resizable(False, False)
            ctk.CTkLabel(s, text="Latest Version Already Installed!").pack(pady=5)
            ctk.CTkButton(s, text="Ok", command=s.destroy, corner_radius=15).pack(pady=5)
            return None
    except Exception as error:
        print(f"Failed to check updates {error}")
        return None

def reading_settings(config):
    with open(config, 'r') as archive:
        settings = json.load(archive)
    return settings

def settings_window():
    settings_window = ctk.CTk()
    settings_window.title("Settings")
    settings_window.geometry("500x250")
    settings_window.iconbitmap("images/icon.ico")
    settings_window.resizable(width=False, height=False)
    settings_window.grid_columnconfigure(0, weight=1)
    settings_window.grid_rowconfigure(0, weight=1)
    # frame = ctk.CTkFrame(settings_window, width=500, height=350, corner_radius=15, fg_color="gray")
    # frame.grid(row=0, column=0, columnspan=2, sticky="ew")

    frame = ctk.CTkFrame(settings_window, corner_radius=15, width=10, height=350)
    frame.place(x=250)

    ctk.CTkLabel(settings_window, text="Version: v2.0.0").grid(row=2, column=1, padx=10, sticky="e")

    themes = ctk.CTkOptionMenu(settings_window, corner_radius=15, values=[""])
    themes.set("Themes (Upcoming)")
    themes.grid(row=0, column=0, padx=10, sticky="w")

    switch_var = ctk.StringVar(value=config["GUI"]["auto_check_for_updates"])
    updates_check = ctk.CTkCheckBox(settings_window, command=checking_updates, variable=switch_var,
                                 text="Auto-Check for updates", onvalue="on", offvalue="off")
    updates_check.grid(row=0, column=1, padx=10, sticky="e")

    if switch_var.get() == "on":
        config["GUI"]["auto_check_for_updates"] = "on"
    else:
        config["GUI"]["auto_check_for_updates"] = "off"

    settings_window.mainloop()

def oppening_path():
    folder_path = "C:\\Windows\\Temp"
    folder_path2 = "C:\\Windows\\Prefetch"
    folder_path3 = f"C:\\Users\\{getting_username()}\\AppData\Local\\Temp"
    os.startfile(folder_path)
    os.startfile(folder_path2)
    os.startfile(folder_path3)

def oppening_recycle_path():
    recycle_path = "C:\\$Recycle.Bin"
    os.startfile(recycle_path)

def oppening_disk():
    disk_path = "C:\\"
    os.startfile(disk_path)

def oppening_github():
    webbrowser.open("https://github.com/PHCavalcante/SWC_Simple_Windows_Cleaner")

title = ctk.CTkLabel(window, text="Simple Windows Cleaner", font=("Segoe UI", 20)).grid(row=0, column=0, sticky="ew")
settingsButton = ctk.CTkButton(window, width=60, text="Settings", corner_radius=15, command=settings_window)
settingsButton.grid(row=1, column=0, padx=10, sticky="e")

helpButton = ctk.CTkButton(window, width=60, text="Help", corner_radius=15, command=help).grid(row=1, column=0, padx=100, pady=10, sticky="e")

tabs = ctk.CTkTabview(window, width=900, height=400, corner_radius=15)
tabs.grid(row=2, column=0, columnspan=2, sticky="ew")
tabs.add("Temporary Files")
tabs.add("Disk Cleanup")
tabs.add("Recycle Bin Cleanup")
tabs.tab("Temporary Files").grid_columnconfigure(0, weight=1)
tabs.tab("Disk Cleanup").grid_columnconfigure(0, weight=1)
tabs.tab("Recycle Bin Cleanup").grid_columnconfigure(0, weight=1)
tabs.tab("Temporary Files").grid_columnconfigure(0, weight=1)

# frame1 = ctk.CTkFrame(tabs.tab("Temporary Files"), width=550, height=380, fg_color="gray", corner_radius=15)
# frame1.grid(row=0, column=0, sticky="nsw")
# frame2 = ctk.CTkFrame(tabs.tab("Temporary Files"), width=200, height=380, fg_color="gray", corner_radius=15)
# frame2.grid(row=2, column=1, sticky="nsw")

textBox = ctk.CTkTextbox(tabs.tab("Temporary Files"), width=450, height=200, corner_radius=15, state="normal")
textBox.insert(0.0, "Temporary Files\n\n" + "Windows Temporary Files are temporary data stored by the operating "
"system and applications during various tasks and processes. These files serve as interim storage for data that is "
"needed for a short duration, such as installation files, updates, and cache. They are created to facilitate faster"
"access to frequently used data, reducing the time it takes for the system and applications to perform certain"
" operations.")
textBox.grid(row=2, column=0, padx=10, pady=25, sticky="w")
textBox = ctk.CTkTextbox(tabs.tab("Disk Cleanup"), width=450, height=200, corner_radius=15, state="normal")
textBox.insert(0.0, "Disk Cleanup\n\n" + "Running a disk cleanup can help you free some storage space by deletting"
" files that's not important to the system or even are some cache or temporary files such as Windows Update cache, "
"thumbnails, internet archives and much more. It's totally safe to run a disk cleanup")
textBox.grid(row=2, column=0, padx=10, pady=25, sticky="w")
textBox = ctk.CTkTextbox(tabs.tab("Recycle Bin Cleanup"), width=450, height=200, corner_radius=15, state="normal")
textBox.insert(0.0, "Recycle Bin Cleanup\n\n" + "As you may know, in the recycle bin are stored all kind of files "
"you delete. take a look in your recycle bin before cleaning it, just to make sore you haven't deleted someting important.\n"
"\nTip: Pressing Shift + Del when deletting a file to permanently delete it so it doesn't go to the recycle bin.")
textBox.grid(row=2, column=0, padx=10, pady=25, sticky="w")
cleanButton = ctk.CTkButton(tabs.tab("Temporary Files"), text="Clean", command=cleaning, width=150, height=40, corner_radius=15)
cleanButton.grid(row=2, column=1, sticky="e")
cleanButton = ctk.CTkButton(tabs.tab("Disk Cleanup"), text="Clean", command=disk_cleanup, width=150, height=40, corner_radius=15)
cleanButton.grid(row=2, column=1, sticky="e")
cleanButton = ctk.CTkButton(tabs.tab("Recycle Bin Cleanup"), text="Clean", command=cleaning_recycle, width=150, height=40, corner_radius=15)
cleanButton.grid(row=2, column=1, sticky="e")

size = (ctk.CTkLabel(tabs.tab("Temporary Files"), text=f"Temporary Files Size: {getting_size()}", corner_radius=15))
size.place(x=650, y=20)
size = (ctk.CTkLabel(tabs.tab("Recycle Bin Cleanup"), text=f"Size of files in Recycle Bin: {getting_recycle_size()}", corner_radius=15))
size.place(x=630, y=20)

openButton = ctk.CTkButton(tabs.tab("Temporary Files"), text="Open Folders", command=oppening_path, corner_radius=15)
openButton.grid(row=3, column=1, pady=10, sticky="e")
openButton = ctk.CTkButton(tabs.tab("Disk Cleanup"), text="Open Folder", command=oppening_disk, corner_radius=15)
openButton.grid(row=3, column=1, pady=10, sticky="e")
openButton = ctk.CTkButton(tabs.tab("Recycle Bin Cleanup"), text="Open Folder", command=oppening_recycle_path, corner_radius=15)
openButton.grid(row=3, column=1, pady=10, sticky="e")

path = ctk.CTkLabel(tabs.tab("Temporary Files"), text=paths(), corner_radius=15, fg_color="white", text_color="black")
path.grid(row=3, column=0, sticky="ew")
path = ctk.CTkLabel(tabs.tab("Disk Cleanup"), text="C:\\", corner_radius=15, fg_color="white", text_color="black")
path.grid(row=3, column=0, sticky="ew")
path = ctk.CTkLabel(tabs.tab("Recycle Bin Cleanup"), text="C:\\$Recycle.Bin", corner_radius=15, fg_color="white", text_color="black")
path.grid(row=3, column=0, sticky="ew")

image = ctk.CTkImage(light_image=Image.open("images\\github_dark.png"),dark_image=Image.open("images\\github_light.png"), size=(15, 15))
image_button = ctk.CTkButton(window, image=image, command=oppening_github ,width=20, height=20, fg_color="transparent", text='').place(x=10, y=10)

switch_var = ctk.StringVar(value="on")

def changing_settings():
    if switch_var.get() == "off":
        ctk.set_appearance_mode("light")
        with open(settings_path, "r", encoding="utf-8") as json_file:
            config = json.load(json_file)
            print(config)

        config["GUI"]["aparence_mode"] = "light"
        print(config)

        with open(settings_path, "w", encoding="utf-8") as json_file:
            json.dump(config, json_file)
    else:
        ctk.set_appearance_mode("dark")
        with open(settings_path, "r", encoding="utf-8") as json_file:
            config = json.load(json_file)
            print(config)

        config["GUI"]["aparence_mode"] = "dark"
        print(config)

        with open(settings_path, "w", encoding="utf-8") as json_file:
            json.dump(config, json_file)

theme_mode = ctk.CTkSwitch(window, onvalue="on", offvalue="off", command=changing_settings, variable=switch_var, text="Dark Mode")
theme_mode.grid(row=1, column=0, padx=10, sticky="w")

with open(settings_path, "r") as json_file:
    config = json.load(json_file)
    if config["GUI"]["auto_check_for_updates"] == "on":
        checking_updates()
    else:
        pass

window.mainloop()
