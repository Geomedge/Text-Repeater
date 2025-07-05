#All The Imports:
import time
import os
import tkinter as tk
from tkinter import messagebox, ttk
from os import system
import webbrowser
import threading
import re
from SAUIGeo import SAU

sauvernr = "1.03.5"
version = "V1.06.1"
sauver = "SAU" + str(sauvernr)
release_date = "05/07/2025"

SAU.check()
var = SAU.start()
print(var)
default = var[0]
button = var[1]
combo = var[2]
cred = var[3]
scale = var[4]
title = var[5]
window_ui = var[6]

def openlink(link):
    link_list = ["https://github.com/Geomedge/Text-Repeater", "https://forms.office.com/r/x7Le5d2bbE", "https://discord.gg/QN5HrTAYYs"]
    webbrowser.open(link_list[link])

def version_info():
    ver_win = tk.Tk()
    ver_win.minsize(250, 125)
    ver_win.title("Version")
    ver_win.config(background="#333")

    l1 = tk.Label(ver_win, text="Version Information", **title)
    l1.pack(side="top", anchor="nw")

    l2 = tk.Label(ver_win, text=f"{version}", **cred)
    l2.pack(side="top")

    l3 = tk.Label(ver_win, text=f"{sauver}", **cred)
    l3.pack(side="top")

    l4 = tk.Label(ver_win, text=f"Release Date : {release_date}", **cred)
    l4.pack(side="top")

#text repeater app
def text_rep():
    root= tk.Tk()
    root.eval('tk::PlaceWindow . centre')
    root.title("Repeater App")
    root.config(background="#333")
    root.minsize("500","325")

    #MENU BAR
    menubar = tk.Menu(root, **window_ui)

    #File Settings
    filemenu = tk.Menu(menubar, tearoff=0, **cred)
    filemenu.add_command(label="Exit", command=root.quit)

    #Settings
    settingsmenu = tk.Menu(menubar, tearoff=0, **cred)

    #Theme Menu
    thememenu = tk.Menu(settingsmenu, tearoff=0, **cred)
    thememenu.add_command(label="Light", command=lambda:[SAU.set(0)])
    thememenu.add_command(label="Dark", command=lambda:[SAU.set(1)])
    thememenu.add_command(label="Mellow", command=lambda:[SAU.set(2)])
    thememenu.add_command(label="Hacker", command=lambda:[SAU.set(3)])

    #Theme Settings
    settingsmenu.add_cascade(label="Choose Theme (Experimental)", menu=thememenu)

    #Help Menu
    helpmenu = tk.Menu(menubar, tearoff=0, **cred)
    helpmenu.add_command(label="Open Discord Support Page", command=lambda:[openlink(2)])
    helpmenu.add_command(label="Open Github Page", command=lambda:[openlink(0)])
    helpmenu.add_separator()
    helpmenu.add_command(label="Report Bugs", command=lambda:[openlink(1)])
    helpmenu.add_separator()
    helpmenu.add_command(label="Version", command=lambda:[version_info()])
    
    #Menubar Itself
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Settings", menu=settingsmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    root.config(menu=menubar)


    l1 = tk.Label(root, text='Text Repeater', **title)
    l1.pack(side="top", anchor="nw")

    #Box 1
    f1 = tk.Frame(root, background='#111')
    l2 = tk.Label(f1, text='Type your Message:', **default)
    l2.pack(side="top",anchor="nw", padx=5, pady=5)

    e1 = tk.Entry(f1, width=40, **button) 
    e1.pack(pady=5, padx=10)
    f1.pack(side='top', anchor='center', pady=5)


    #Box 2
    f2 = tk.Frame(root, background='#111')
    l3 = tk.Label(f2, text='How many times should it be repeated?', **default)
    l3.pack(side="top",anchor="nw", padx=5, pady=5)

    e2 = tk.Spinbox(f2, from_=0, to=100000, width=39, **button)
    e2.pack(pady=5, padx=10)
    f2.pack(side='top', anchor='center', pady=5)
    
    def a():
        try:
            x1 = e1.get()
            try:
                x2 = int(e2.get())
                path = os.path.expanduser("~") + r"\Documents\Repeated text.txt"
                myfile = open(path, "a")
                for i in range(x2):
                    myfile.write(x1)
                    myfile.write("\n")
                myfile.close
                messagebox.showinfo("Done!", f"Task Completed Successfully!\nFile Saved : {path}")
            except:
                messagebox.showerror("Error", "Invalid Number Selected / No Number Found!")
        except:
            messagebox.showerror("Error!", "Invalid Text!")
    
    b1 = tk.Button(root, text='Create File!', command=lambda:[threading.Thread(target=a).start()], **button)
    b1.pack(pady=5)

    # Credits
    ver = tk.Label(root, text=version, **cred)
    ver.pack(side='left', anchor='sw', padx=5, pady=5)
    
    credit = tk.Label(root, text="Made By Geomedge", **cred)
    credit.pack(side='right', anchor='se', padx=5, pady=5)


    root.mainloop()

text_rep()