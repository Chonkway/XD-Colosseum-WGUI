from pathlib import Path
import subprocess
from sys import stdin, stdout
from tkinter.constants import TRUE
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run
from PySimpleGUI.PySimpleGUI import Menu, Output, TabGroup, ToolTip, Window
import new_menus
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



#--- Window Definition ---#
window = sg.Window('Pokemon XD/Colosseum Test GUI', WindowDef.maintabgrp, alpha_channel=0.95)





while True: #// Event loop
    
    event, value = window.read()
    print(event, value)
     #// values[1] is where the tabgroup returns the menu being accessed, using this for navigation
    if value[1] == 'Random':
        new_menus.Menu(process, event, value).RandomMenu()

    if event == sg.WIN_CLOSED or event == 'Close':
        break

window.close()

#// Randomizer menu always selects Move Types to be randomized