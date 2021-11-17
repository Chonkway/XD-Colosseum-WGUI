from pathlib import Path
import subprocess
from sys import stdin, stdout
from tkinter.constants import TRUE
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run
from PySimpleGUI.PySimpleGUI import Menu, Output, ToolTip, Window
import menus
import WindowDef

#----------------

#// Should keep a persistent value of this eventually so users don't have to reselect everytime they run the tool in later version
iso_path = sg.PopupGetFile('Point to the path of your ISO')

process = subprocess.Popen(["GoD-Tool.exe", '/c', iso_path], text=True, stdin=subprocess.PIPE, shell=True)


def Toolbar():
    """
    Easy way to edit toolbar info
    """
    if event == 'About...':
        sg.Popup("GoD Tool V2.4.4\nby Stars Momodu\nTwitter: @StarsMmd | Discord: Stars#4434\nsource code:\n https://github.com/PekanMmd/Pokemon-XD-Code.git\n\n")



#--- Window Definitions ---#
window = sg.Window('Pokemon XD/Colosseum Test GUI', WindowDef.layout, alpha_channel=0.95)

window2 = sg.Window('Pokemon XD/Colosseum Test GUI - Utility Window', WindowDef.utilmenu, modal=True, resizable=True,
            alpha_channel=0.95)

window3 = sg.Window('Pokemon XD/Colosseum Test GUI - Randomizer Window', WindowDef.randommenu, modal=True, resizable=True,
            alpha_channel=0.95)

window4 = sg.Window('Pokemon XD/Colosseum Test GUI - Patches Window', WindowDef.patchmenu, modal=True, resizable=True,
            alpha_channel=0.95)

window5 = sg.Window('Pokemon XD GoD/Colosseum Test GUI - Import/Export Menu', WindowDef.ImpExpMenu, modal=True, resizable=True,
            alpha_channel=0.95, element_justification='center')
# ---- 







while True: #// Event loop

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'About...':
        Toolbar()

    if event[0] == '4':
        menus.Menu(process, window5).ImportExportMenu()
    if event[0] == '6':
        menus.Menu(process, window4).PatchesMenu()
    if event[0] == '7': #// Open Utility Menu
        menus.Menu(process, window2).UtilityMenu()
    if event[0] == '8':
        menus.Menu(process, window3).RandomMenu()
    else:
        menus.Menu(process, window).MainMenu()

window.close()





"""
Checklist


-Reroute stdout to debug windows
-Clean up code
-Create a cleaner theme
-Find a way for the windows to be reopened at any time

"""