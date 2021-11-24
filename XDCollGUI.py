from os import pipe, write
from pathlib import Path
import subprocess
from sys import stdin, stdout
from tkinter.constants import TRUE
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run
from PySimpleGUI.PySimpleGUI import Menu, Output, TabGroup, ToolTip, Window
import WinDef
import MenuFunctions
#----------------

#// Should keep a persistent value of this eventually so users don't have to reselect everytime they run the tool in later version
iso_path = sg.PopupGetFile('Point to the path of your ISO')

process = subprocess.Popen(["GoD-Tool.exe", iso_path], text=True, stdin=subprocess.PIPE)


def Toolbar():
    """
    Easy way to edit toolbar info
    """
    if event == 'About...':
        sg.Popup("GoD Tool V2.4.4\nby Stars Momodu\nTwitter: @StarsMmd | Discord: Stars#4434\nsource code:\n https://github.com/PekanMmd/Pokemon-XD-Code.git\n\n")



#--- Window Definition ---#
window = sg.Window('Pokemon XD/Colosseum Test GUI', WinDef.maintabgrp, alpha_channel=0.95, resizable=True)












while True:
    event, values = window.read()
    if values['MainMenu'] == 'EditingTools':
        MenuFunctions.MenuFunction(process, event, values).EditingMenu()

    if values['MainMenu'] == 'Randomizer':
        MenuFunctions.MenuFunction(process, event, values).RandomMenu()

    if values['MainMenu'] == 'PatchOptions':
        MenuFunctions.MenuFunction(process, event, values).PatchMenu()
    
    if values['MainMenu'] == 'Import/Export':
        MenuFunctions.MenuFunction(process, event, values).ImportExport()

    if values['MainMenu'] == 'UtilityMenu':
        MenuFunctions.MenuFunction(process, event, values).UtilityMenu()

    if values['MainMenu'] == 'AllDataTables':
        MenuFunctions.MenuFunction(process, event, values).DataTables()

    if event == sg.WIN_CLOSED or event == 'Close':
        break
window.close()

#// Randomizer menu always selects Move Types to be randomized and I have no clue why...it prints the correct values 