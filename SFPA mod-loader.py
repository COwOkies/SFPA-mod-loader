import os
import tkinter as tk
import shutil

print("log window\n-----------\n")
    
def button_pressed(button):
    if button.cget("bg") == '#ffea00': ext=".swp"
    else: ext=".swf"
    replaceMod(button.cget("text"),ext)
    
def replaceMod(modname,ext):

    modname=str(modname)+ext
    shutil.copy("files\\"+modname,"game\SFPA.swf")
    print("Replacing SFPA.swf with "+modname)
    launchGame()

def launchGame():
    print("Killing SFPA.exe if running :\n")
    os.system('tasklist | find /i "SFPA.exe" && taskkill /im SFPA.exe /F || echo process "SFPA.exe" not running.')
    print("\nLaunching game...")
    os.startfile(r'game\SFPA.exe')

window = tk.Tk()
window.title("SFPA mod-loader")
window.configure(bg='#ffc800')
window.iconbitmap("fancy.ico")


mods = os.listdir(r'files')
text_list = []

tk.Label(window, text="Mod List",bg='#ffc800',font=("Verdana", 15,"bold")).pack(side="top",fill="x")


for mod in mods:
    if str(mod[-4:]) == ".swf" or str(mod[-4:]) == ".swp":
        modname = str(mod)[:-4]
        button = tk.Button(window, text=modname,bg='#ffaa00',font=("Verdana", 13))
        if str(mod[-4:]) == ".swp": button.config(bg='#ffea00')
        button.config(command=lambda button=button: button_pressed(button))
        button.pack(side="top", fill="x", expand=True)
        text_list.append(button)

infolabel = tk.Label(window, text="Please select a mod",bg='#ffc800',font=("Verdana", 11))

infolabel.pack()
window.mainloop()
