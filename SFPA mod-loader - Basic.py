#imports
import os; import tkinter as tk; import shutil

#Setup Tkinter
window = tk.Tk();window.title("SFPA mod-loader");window.configure(bg='#ffc800');window.iconbitmap("fancy.ico")

#replaceMod function
def replaceMod(button):
    modname = str(button.cget("text"))+".swf"
    shutil.copy("files\\"+modname,"game\SFPA.swf"); print("Replacing SFPA.swf with "+modname)
    print("Launching game...\n______________________\n");os.startfile(r'game\SFPA.exe')

#Title (Mod List)
tk.Label(window, text="Mod List",bg='#ffc800',font=("Verdana",15,"bold")).pack()

#Setup mods buttons
mods = os.listdir(r'files')
for mod in mods:
    if str(mod[-4:]) == ".swf":
        modname = str(mod)[:-4]
        button = tk.Button(window, text=modname,bg='#ffaa00',font=("Verdana", 13))
        button.config(command=lambda button=button: replaceMod(button))
        button.pack(side="top", fill="x", expand=True)

#tkinter loop
window.mainloop()
