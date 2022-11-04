#imports
import os; import tkinter as tk; import shutil

#Setup Tkinter and log text
window = tk.Tk(); window.title("SFPA mod-loader"); window.configure(bg='#ffc800'); window.iconbitmap("fancy.ico")
print("log window\n-----------\n")

#functions
def replaceMod(button):
    if button.cget("bg") == '#ffdd00': ext=".swp"
    else: ext=".swf"
    modname=str(button.cget("text"))+ext
    shutil.copy("files\\"+modname,"game\SFPA.swf"); print("Replacing SFPA.swf with "+modname)
    print("Killing SFPA.exe if running :")
    os.system('tasklist | find /i "SFPA.exe" && taskkill /im SFPA.exe /F || echo process "SFPA.exe" not running.')
    changeGameTitle(button.cget("text"))
    os.startfile(r'game\SFPA.exe'); print("\nLaunching game.")

def changeGameTitle(name):
    with open(r'game\META-INF\AIR\application.xml', 'r') as file:
        data = file.readlines()
    data[14] = '    <name>'+name+'</name>\n'
    with open(r'game\META-INF\AIR\application.xml', 'w') as file:
        file.writelines(data)

#Title (Mod List)
tk.Label(window, text="Mod List",bg='#ffc800',font=("Verdana", 15,"bold")).pack(side="top",fill="x")

#Setup mods buttons
mods = os.listdir(r'files')
for mod in mods:
    if str(mod[-4:]) == ".swf" or str(mod[-4:]) == ".swp":
        modname = str(mod)[:-4]
        button = tk.Button(window, text=modname,bg='#ffc800',font=("Verdana", 13))
        if str(mod[-4:]) == ".swp": button.config(bg='#ffdd00',font=("Verdana", 13,"italic"))
        button.config(command=lambda button=button: replaceMod(button))
        button.pack(side="top", fill="x", expand=True)

#Label+TK loop
tk.Label(window, text="Please select a mod",bg='#ffc800',font=("Verdana", 11)).pack()
window.mainloop()
