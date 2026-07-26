from tkinter import *
from getpass import *
import platform

folderuser = getuser()
appname = f"Welcome {folderuser}!"
caths = 0
topshown = True

globalbg = "#252525"
globalfg = "#FFFFFF"

def alwaysontop(show):
    if show == True:
        Frame(root, bg="#151515", height=25, width=500).place(x=0,y=0)
        Button(root,text=" Info ", bg="#151515", fg=globalfg, border=0, command=infopage).place(x=5, y=2)
        Button(root,text=" Create a backup ", bg="#151515", fg=globalfg, border=0, command=backup).place(x=40, y=2)
        Button(root, text=" Use a Backup drive ", bg='#151515', fg=globalfg, border=0, command=backdown).place(x=135, y=2)

def backup():
    global caths
    caths = 1
    cath(caths)

def backdown():
    global caths
    caths = 2
    cath(caths)

def cath(page):
    for widget in root.winfo_children():
        widget.destroy()

    global appname
    root.geometry("500x400")
    root.resizable(False, False)
    root.configure(bg=globalbg)
    root.iconbitmap('Assets/main.ico')
    if page == 0:
        Label(root, text=f"Welcome {folderuser}!", bg=globalbg, fg=globalfg, font=("Arial",15,"bold")).place(x=5, y=25)
        Label(root, text="What do you need?", bg=globalbg, fg=globalfg, font=("Arial",10,"bold")).place(x=5, y=50)
    elif page == 1:
        appname = "Creating a BackUp"
    elif page == 2:
        appname = "Use a BackUp Drive"
    
    root.title(f"Project BackUp - {appname}") #I'm a dumbass
    alwaysontop(topshown)


def infopage(): # Finished, do not touch
    info = Toplevel()
    info.title("Project BackUp - Information")
    info.geometry("400x100")
    info.resizable(False, False)
    info.iconbitmap("assets/main.ico")
    info.configure(bg=globalbg)

    edition = platform.version()
    release = platform.release()
    system = platform.system()
    host = platform.node()
    ty_pe = platform.machine()
    arch = platform.architecture()
    pros = platform.processor()

    Label(info, text=f"{system} {release}\nVersion: {edition}\nComputer name: {host}\nDevice type: {ty_pe}\nAchitecture: {arch}\nProcessor: {pros}", bg=globalbg, fg=globalfg).pack(padx=20)

root = Tk()

cath(caths)
root.mainloop()