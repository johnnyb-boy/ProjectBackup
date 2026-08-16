from tkinter import *
from tkinter import messagebox
from getpass import *
import platform
import ctypes
import os

folderuser = getuser()
appname = f"Welcome {folderuser}!"
caths = 0
topshown = True

globalbg = "#252525"
globalfg = "#FFFFFF"
ver = '0.0.2b'
adminpriv = ''

is_admin = ctypes.windll.shell32.IsUserAnAdmin()
if is_admin:
    adminpriv = "[ADMIN]"



def alwaysontop(show):
    if show == True:
        Frame(root, bg="#151515", height=25, width=500).place(x=0,y=0)
        Button(root,text=" Info ", bg="#151515", fg=globalfg, border=0, command=infopage).place(x=5, y=2)
        Button(root,text=" Create a backup ", bg="#151515", fg=globalfg, border=0, command=backup).place(x=40, y=2)
        Button(root, text=" Use a Backup drive ", bg='#151515', fg=globalfg, border=0, command=backdown).place(x=135, y=2)

def github():
    print("Github here")

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
        Label(root, text=f"V{ver}", bg=globalbg, fg=globalfg, font=("Arial",8,"bold")).place(x=455, y=25)
        Button(root, text="ProjetBackUp by JohnnyB-boy", bg=globalbg, fg="#3B3B3B", font=("Arial",7,"bold"), border=0, command=github).place(x=5, y=375)
    elif page == 1:
        appname = "Creating a BackUp"
        Label(root, text="Creating a BackUp", bg=globalbg, fg=globalfg, font=("Arial", 15, "bold")).place(x=5, y=25)
        if not is_admin:
            Label(root, text="Admin is required for the Appdata file, an other account or for an other hard drive", bg=globalbg, fg=globalfg, font=("Arial", 8, "bold")).place(x=5, y=50)
            Label(root, text="This user", )
            Checkbutton(root, variable=This_user, bg=globalbg, border=0).place(x=0,y=100)
    elif page == 2:
        appname = "Use a BackUp Drive"
    
    root.title(f"Project BackUp - {appname} {adminpriv}") #I'm a dumbass
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
from defaultvar import *
dist_user.set(getuser())
tar_disk.set(os.environ["SystemDrive"])
print(f"{This_user},{This_Disk},{user_all},{Desktop},{Docs},{music},{video},{image},{d3},{dist_user},{tar_disk}")
cath(caths)
root.mainloop()
messagebox.showinfo("Project BackUp", "Thanks you for using Project BackUp.\nBy using it, you're contribuing to his developpement! \n\n- JohnnyB-Boy") #text here