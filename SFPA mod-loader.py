import os
import tkinter as tk
import shutil

print("log window\n-----------\n")
    
def button_pressed(button):
    replaceMod(button.cget("text"))
    
def replaceMod(modname):
    modname = str(modname)+".swf"
    if (os.path.isfile(r'game\SFPA.swf')):
        os.remove(r'game\SFPA.swf')
        print("'game\SFPA.swf' deleted")
    else: print("'game\SFPA.swf' doesn't exist")

    
    shutil.copy("files\\"+modname,"game")
    print("'files\\"+modname+"' copied to 'game' folder")
    
    os.rename(r'game\\'+modname,r'game\SFPA.swf')
    print("'"+modname+"' renamed to SFPA.swf")
    launchGame()

def launchGame():
    os.system("TASKKILL /F /IM SFPA.exe")
    print("Launching game...")
    os.startfile(r'game\SFPA.exe')

window = tk.Tk()
window.title("SFPA mod-loader")
window.configure(bg='#ffc800')
window.iconbitmap("fancy.ico")

mods = os.listdir(r'files')
text_list = []

tk.Label(text="Mod List",bg='#ffc800',font=("Verdana", 15,"bold")).pack()


for mod in mods:
    if str(mod[-4:]) == ".swf":
        mod = str(mod)[:-4]
        button = tk.Button(window, text=mod,bg='#ffaa00',font=("Verdana", 13))
        button.config(command=lambda button=button: button_pressed(button))
        button.pack(side="top", fill="both", expand=True)
        text_list.append(button)

infolabel = tk.Label(text="Please select a mod",bg='#ffc800',font=("Verdana", 11))

infolabel.pack()
window.mainloop()
