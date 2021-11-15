import subprocess
from sys import stdin, stdout
from tkinter.constants import TRUE
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run
from PySimpleGUI.PySimpleGUI import Menu, Output, ToolTip
import menus
import WindowDef

#----------------

process = subprocess.Popen("GoD-Tool.exe XDGoD.iso", text=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=STDOUT)

def BackToMain():
    #// This is my lazy solution to navigating to the main menu.
    for i in range(0,3):
        print('0', file=process.stdin)
        process.stdin.flush()


#--- Window Definitions ---#
window = sg.Window('Pokemon XD/Colosseum Test GUI', WindowDef.layout, alpha_channel=0.95)

window2 = sg.Window('Pokemon XD/Colosseum Test GUI - Utility Window', WindowDef.utilmenu, alpha_channel=0.95)

window3 = sg.Window('Pokemon XD/Colosseum Test GUI - Randomizer Window', WindowDef.randommenu, alpha_channel=0.95)

window4 = sg.Window('Pokemon XD/Colosseum Test GUI - Patches Window', WindowDef.patchmenu, alpha_channel=0.95)
# ---- 








while True: #// Event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Utilities': #// Open Utility Menu
        menus.Menu(process, window2).UtilityMenu()
    if event == 'Randomizer':
        menus.Menu(process, window3).RandomMenu()

window.close()




