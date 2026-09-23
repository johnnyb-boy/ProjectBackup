import getpass, shutil, os, time
import tkinter as tk
from tkinter import ttk

user = getpass.getuser()
drive = os.environ["SystemDrive"]

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def ui(w):
    clear_window()
    if w == 0:
        tk.Button(root, text="Start Clone", command=lambda: clonesetup()).pack(padx=20, pady=20)

def clonesetup():
    clonestart(drive,"Desktop", "D:/")  # on saute le ui(-1) inutile, clear_window() est déjà dans clonestart

def clonestart(letter,directory, dest):
    clear_window()
    contenu = os.listdir(f"{letter}/Users/{user}/{directory}")
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode='determinate')
    progress.place(x=50, y=200)

    files, dirs = [], []
    chemin = os.path.expanduser(f"{letter}/Users/{user}/{directory}")
    for element in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, element)
        if os.path.isfile(chemin_complet):
            files.append(element)
        elif os.path.isdir(chemin_complet):
            dirs.append(f"{element}/")

    progress["maximum"] = len(files)  # plus réaliste pour un test visuel
    for i in range(progress["maximum"]):
        shutil.copy(f"{letter}/Users/{user}/{directory}/{files[i]}", dest)
        progress["value"] = i + 1
        root.update_idletasks()
        time.sleep(0.02)  # ajoute un délai pour VOIR la progression

    progress["maximum"] = len(dirs)  # plus réaliste pour un test visuel
    for i in range(progress["maximum"]):
        shutil.copy(f"{letter}/Users/{user}/{directory}/{dirs[i]}", dest)
        progress["value"] = i + 1
        root.update_idletasks()
        time.sleep(0.02)  # ajoute un délai pour VOIR la progression
    
    print(len(contenu))

root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)

ui(0)

root.mainloop()