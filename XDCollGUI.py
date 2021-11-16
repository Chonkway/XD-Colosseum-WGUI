import subprocess
from sys import stdin, stdout
from tkinter.constants import TRUE
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run
from PySimpleGUI.PySimpleGUI import Menu, Output, ToolTip
import menus
import WindowDef

#----------------

process = subprocess.Popen("GoD-Tool.exe XDGoD.iso", text=True, stdin=subprocess.PIPE, bufsize=1)


def Toolbar():
    """
    Easy way to edit toolbar info
    """
    if event == 'About...':
        sg.Popup("GoD Tool V2.4.4\nby Stars Momodu\nTwitter: @StarsMmd | Discord: Stars#4434\nsource code:\n https://github.com/PekanMmd/Pokemon-XD-Code.git")


#--- Window Definitions ---#
window = sg.Window('Pokemon XD/Colosseum Test GUI', WindowDef.layout, alpha_channel=0.95)

window2 = sg.Window('Pokemon XD/Colosseum Test GUI - Utility Window', WindowDef.utilmenu, modal=True, resizable=True,
            alpha_channel=0.95)

window3 = sg.Window('Pokemon XD/Colosseum Test GUI - Randomizer Window', WindowDef.randommenu, modal=True, resizable=True,
            alpha_channel=0.95)

window4 = sg.Window('Pokemon XD/Colosseum Test GUI - Patches Window', WindowDef.patchmenu, modal=True, resizable=True,
            alpha_channel=0.95)
# ---- 








while True: #// Event loop

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'About...':
        Toolbar()

    if event == 'Utilities': #// Open Utility Menu
        menus.Menu(process, window2).UtilityMenu()
    if event == 'Randomizer':
        menus.Menu(process, window3).RandomMenu()
    if event == 'Patches':
        menus.Menu(process, window4).PatchesMenu()
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