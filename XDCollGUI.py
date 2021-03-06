from math import log
import os
from pathlib import Path
import subprocess
import sys
import time
from sys import stdin, stdout
from tkinter.constants import TRUE
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run
from PySimpleGUI.PySimpleGUI import Menu, Output, TabGroup, ToolTip, Window
import WinDef
import MenuFunctions
#----------------

#// Gimmicky way of locating logfiles, attempts to locate the iso name and uses that to create the logdir for reading stdout
iso_path = sg.PopupGetFile('Point to the path of your ISO', history=True, file_types=(("ISO Files", ".iso"),))


process = subprocess.Popen(["GoD-Tool.exe", iso_path], text=True, shell=True, stdin=subprocess.PIPE)


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

#------Gimmicky way to access the logfiles for the Tool to mimic reading stdout
    fileName = os.path.basename(iso_path)
    fileNameStrip = str(fileName).replace('.iso', '')
    logdir = Path(str(fileNameStrip) + ' GoD Tool' + '\\Logs')
    logfiles = sorted([ f for f in os.listdir(logdir)])
#----------------------------------------------------------------------
    def MultiLine():
        with open(str(logdir) + '\\' + str(logfiles[0]), 'r') as multiline: #// Should point to the most recent logfile being generated, looking to mimic tail-f
            print(multiline.read())




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

    if values['MainMenu'] == 'AllDataTables':   #// Also saving options from stdin that should be flushed (ie all buttons send 9 first)
        MenuFunctions.MenuFunction(process, event, values).DataTables(MultiLine)
        
    if event == sg.WIN_CLOSED or event == 'Close':
        break
window.close()

#// Randomizer menu always selects Move Types to be randomized and I have no clue why...it prints the correct values 