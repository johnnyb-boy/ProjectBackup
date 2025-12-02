import tkinter
import plyer
import platform
import ctypes
import getpass
import zipfile
from tkinter import messagebox
import os

root = tkinter.Tk()
appdat = tkinter.IntVar()
lettre = os.environ["SystemDrive"]

mode = 0
user = getpass.getuser()
user_exist = True
is_admin = ctypes.windll.shell32.IsUserAnAdmin()

This_user_checkmark = tkinter.IntVar()
Desktop_checkmark = tkinter.IntVar()
Document_checkmark = tkinter.IntVar()
Image_checkmark = tkinter.IntVar()
Music_checkmark = tkinter.IntVar()
Video_checkmark = tkinter.IntVar()
Download_checkmark = tkinter.IntVar()
D3_checkmark = tkinter.IntVar() # 3D - mis sur False car pas tout les pc l'ont.
usern = tkinter.StringVar() # J'ai jamais tester StringVar() mais sa doit étre sa.

This_user_checkmark.set(1)
Desktop_checkmark.set(1)
Document_checkmark.set(1)
Image_checkmark.set(1)
Music_checkmark.set(1)
Video_checkmark.set(1)
Download_checkmark.set(1)
D3_checkmark.set(0)
appdat.set(0)
usern.set(user)

def pcinfo():
    edition = platform.version()
    release = platform.release()
    system = platform.system()
    host = platform.node()
    ty_pe = platform.machine()
    arch = platform.architecture()
    pros = platform.processor()
    
    infopc = tkinter.Toplevel(root)
    infopc.title("Info")
    infopc.geometry("400x100")
    infopc.resizable(False, False)
    infopc.iconbitmap("assets/icon.ico")
    infopc.configure(bg="#202020")
    tkinter.Label(infopc, text=f"{system} {release}\nVersion: {edition}\nPC Name: {host}\nDevice Type: {ty_pe}\nAchitecture: {arch}\nProcessor: {pros}", bg="#202020", fg="#FFFFFF").pack(padx=20)

def backup_page():
    global mode
    if not mode == 1:
        tkinter.Frame(root, bg="#202020", width=600,height=570).place(x=0, y=30)
        mode = 1
        main()

def loadup_page():
    global mode
    if not mode == 2:
        tkinter.Frame(root, bg="#202020", width=600,height=570).place(x=0, y=30)
        mode = 2
        main()

def Start():
    global This_user_checkmark
    global Desktop_checkmark
    global Document_checkmark
    global Image_checkmark
    global Music_checkmark
    global Video_checkmark
    global Download_checkmark
    global D3_checkmark
    global appdat
def useroption():
    global This_user_checkmark
    global is_admin
    if This_user_checkmark.get() == 0:
        tkinter.Label(root, text="User Name:", bg="#202020", fg="#FFFFFF").place(x=5, y=100)
        username = tkinter.Entry(root, width=50, border=0)
        username.place(x=70, y=103)
        username.insert(0, user)
    else:
        tkinter.Frame(root, width=370, height=40, bg="#202020").place(x=5,y=100)

def replyask():
    infopc = tkinter.Toplevel(root)
    infopc.title("Where does this name came from ?")
    infopc.geometry("300x50")
    infopc.resizable(False, False)
    infopc.iconbitmap("assets/icon.ico")
    infopc.configure(bg="#202020")
    tkinter.Label(infopc, text=f"{user} is set as your username because\nyour user path is: {lettre}/Users/{user}", bg="#202020", fg="#F0F0F0").pack(padx=20)

def admin():
    global This_user_checkmark
    global appdat
    if This_user_checkmark.get() == 1 and appdat.get() == 0:
        Start()
    else:
        if is_admin:
            if not This_user_checkmark:
                user = username.get()
            else:
                user = getpass.getuser()
                
            user_path = f"{lettre}Users\\{user}"
            if not os.path.isdir(user_path):
                messagebox.showerror("Error", f"The user '{user}' does not exist.")
                return
            else:
                messagebox.showerror("GoodNews", f"The user '{user}' does exist.")
                return
            Start()
        else:
            messagebox.showerror("Error", "Admin permission require.\nPlease,Reboot the App as Admin") # ceci est maintenant innutile mais au cas ou y'a un bugé
            
def main():
    global mode
    tkinter.Frame(root, bg="#151515", width=600, height=30).place(x=0, y=0)
    tkinter.Button(root, text="Device Info", bg="#252525", fg="#FFFFFF", border=0, command=pcinfo).place(x=5, y=5)
    tkinter.Button(root, text="Create BackUp", bg="#252525", fg="#FFFFFF", border=0, command=backup_page).place(x=75, y=5)
    tkinter.Button(root, text="Load BackUp", bg="#252525", fg="#FFFFFF", border=0, command=loadup_page).place(x=165, y=5)
    if mode == 0:
        tkinter.Label(root, text=f"Hello {user}.\n\nWhat's New ?",bg="#202020", fg="#FFFFFF", font=("Arial", 20, "bold")).place(x=5,y=30)
        tkinter.Button(root, text="Where does this name came from ?",bg="#202020", fg="#0050FF", border=0, borderwidth=0, command=replyask).place(x=5,y=60)
    elif mode == 1:
        if is_admin:
            root.title("BackUpAll - Create BackUp [ADMIN]")
        else:
            root.title("BackUpAll - Create BackUp")
        tkinter.Label(root, text="Create a BackUp",bg="#202020", fg="#FFFFFF", font=("Arial", 20, "bold")).place(x=5,y=30)
        if is_admin:
            tkinter.Checkbutton(root, bg="#202020",variable=This_user_checkmark, border=0, command=useroption).place(x=5, y=80)
            tkinter.Label(root, text="This user ?", bg="#202020", fg="#FFFFFF").place(x=25,y=83)
        else:
            tkinter.Label(root, text="Since this application is not admin, you cannot choose a user and use appdata", bg="#202020", fg="#FFFFFF").place(x=5,y=83)
        tkinter.Checkbutton(root, bg="#202020",variable=Desktop_checkmark, border=0).place(x=5, y=140)
        tkinter.Label(root, text="Desktop", bg="#202020", fg="#FFFFFF").place(x=25,y=143)
        tkinter.Checkbutton(root, bg="#202020",variable=Document_checkmark, border=0).place(x=5, y=160)
        tkinter.Label(root, text="Documents", bg="#202020", fg="#FFFFFF").place(x=25,y=163)
        tkinter.Checkbutton(root, bg="#202020",variable=Image_checkmark, border=0).place(x=5, y=180)
        tkinter.Label(root, text="Images", bg="#202020", fg="#FFFFFF").place(x=25,y=183)
        tkinter.Checkbutton(root, bg="#202020",variable=Music_checkmark, border=0).place(x=5, y=200)
        tkinter.Label(root, text="Musics", bg="#202020", fg="#FFFFFF").place(x=25,y=203)
        tkinter.Checkbutton(root, bg="#202020",variable=Video_checkmark, border=0).place(x=5, y=220)
        tkinter.Label(root, text="Video", bg="#202020", fg="#FFFFFF").place(x=25,y=223)
        tkinter.Checkbutton(root, bg="#202020",variable=Download_checkmark, border=0).place(x=5, y=240)
        tkinter.Label(root, text="Downloads", bg="#202020", fg="#FFFFFF").place(x=25,y=243)
        tkinter.Checkbutton(root, bg="#202020",variable=D3_checkmark, border=0).place(x=5, y=260)
        tkinter.Label(root, text="3D", bg="#202020", fg="#FFFFFF").place(x=25,y=263)
        if is_admin:
            tkinter.Checkbutton(root, bg="#202020", variable=appdat, border=0).place(x=5, y=280)
            tkinter.Label(root, text="App Datas (The application will need admin)", bg="#202020", fg="#FFFFFF").place(x=25,y=283)
        START = tkinter.Button(root, text=" Start ", bg="#252525", fg="#FFFFFF", border=0, command=admin).place(y=320, x=290)
    elif mode == 2:
        if is_admin:
            root.title("BackUpAll - Load BackUp [ADMIN]")
        else:
            root.title("BackUpAll - Load BackUp")
        tkinter.Label(root, text="Load a BackUp",bg="#202020", fg="#FFFFFF", font=("Arial", 20, "bold")).place(x=5,y=30)
        if is_admin:
            tkinter.Checkbutton(root, bg="#202020",variable=This_user_checkmark, border=0, command=useroption).place(x=5, y=80)
            tkinter.Label(root, text="This user ?", bg="#202020", fg="#FFFFFF").place(x=25,y=83)
        else:
            tkinter.Label(root, text="Since this application is not admin, you cannot choose a user", bg="#202020", fg="#FFFFFF").place(x=5,y=83)
if is_admin:
    root.title("BackUpAll [ADMIN]")
else:
    root.title("BackUpAll")
root.geometry("600x400")
root.configure(bg="#202020")
root.resizable(False, False)
root.iconbitmap("assets/icon.ico")
main()
print("L'application a demarrer.")
root.mainloop()